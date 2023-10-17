# data related dependencies 
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import sys


class etl:

    def __init__(self, condition, url=None):

        # Condition = test, testing conditons 
        # Condition = production, pulls the data from actual api endpoint


        print('Etl Pipeline')
        print('--'*25)
        self.url = url
        self.condition = condition 

    def extract(self):
        
        if self.condition == 'test':
            data = pd.read_csv('./data/test/shelter1000.csv')
            
        else:
            # https://data.austintexas.gov/resource/9t4d-g238.json
            try:
                data = pd.read_json(self.url)
            except:
                raise "Data Source Not Specified."
            

        print("Data Received!")
        print('--'*25)

        return data

   
   
    def transform(self, data):


        print('Transforming Data.')

        labels = ['- Converting datetime and date_of_birth to datetime objects and transforming them to the pattern mm/dd/yyyy',
                '- Filling NA.',
                '- Creating ID for Outcome type and Outcome Event Type.',
                '- Dividing into Entities']

        print(labels[0])


        print(labels[1])

        data.fillna('Not Recorded',inplace=True)

        print(labels[2])

        data['outcome_type_id'] = data.index + 1
        data['outcome_event_id'] = data.index + 1

        print(labels[3])

        # Dividing into entities 
        animal_table = ['animal_id', 'breed', 'color', 'name','date_of_birth','animal_type']
        outcome_table = ['outcome_type_id','outcome_type']
        outcome_event = ['outcome_event_id','datetime','sex_upon_outcome','outcome_subtype','animal_id','outcome_type', 'outcome_type_id']
        data_colums_order = ['animal_id','outcome_type_id','outcome_event_id']


        # re-ordering
        animal = data[animal_table]
        outcomes = data[outcome_table]
        outcome_events = data[outcome_event]
        data = data[data_colums_order]


        # Correcting Duplication
        animal.drop_duplicates(inplace=True)
        outcomes = pd.DataFrame(pd.Series(outcomes['outcome_type'].unique(),name='outcome_type'))
        outcomes['outcome_type_id'] = outcomes.index + 1 
        outcomes = outcomes[['outcome_type_id','outcome_type']]

        # Mapping Outcome_id to Outcome type
        outcome_mapper = dict(zip(outcomes['outcome_type'],outcomes['outcome_type_id']))
        outcome_events['outcome_type_id']= outcome_events['outcome_type'].map(outcome_mapper)
        outcome_events = outcome_events.drop('outcome_type', axis=1)


        print('Data Transformed.')
        print('--'*25)

        return data, animal, outcomes, outcome_events

       


    def load(self, transformed_data: list):
        
        print('Received transformed data.')

        fact_table, animal, outcomes, outcome_events = transformed_data

        # print(animal)
        print('--'*25)
        print('- Firing up Postgres')

        print('- Connection Established.')
        
        

        DATABASE_URL = "postgresql+psycopg2://r0han:cicada3301@db:5432/shelter"

        engine = create_engine(DATABASE_URL)

        animal.to_sql('animal', engine, if_exists='append', index=False)
        outcomes.to_sql('outcome_type', engine, if_exists='append', index=False)
        outcome_events.to_sql('outcome_event', engine, if_exists='append', index=False)
        fact_table.to_sql('fact_table', engine, if_exists='replace', index=False)

        print('- Loading Data')
        print('--'*25)
        print('Data Load Completed.')




    def display(self, data, lines=10):

        print(data.head(lines))


if __name__ == '__main__':

    # Data Source 
    args = sys.argv
    data_url = args[1]

    # etl_obj
    etl_obj = etl(condition="production", url=data_url)

    data = etl_obj.extract()
    transformed_data = etl_obj.transform(data) # returns transformed 

    #print([df.head(2) for df in transformed_data[1:]])

    etl_obj.load(transformed_data) # takes transformed data



