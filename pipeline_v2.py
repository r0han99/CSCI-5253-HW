# data related dependencies 
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


class etl:

    def __init__(self, condition):


        print('Etl Pipeline')
        print('--'*25)
        self.condition = condition 

    def extract(self):
        
        if self.condition == 'test':
            data = pd.read_json('https://data.austintexas.gov/resource/9t4d-g238.json')
            
        else:
            print('- API endpoint read configuration is not set. Complete the code.')

        print("Data Received!")
        print('--'*25)

        return data

    def transform(self, data):

        
        '''
            - month year to separate columns, months to month names
            - date time and date_of_birth to just date mm/dd/yy 
            - drop outcome_subtype
        '''

        print('Transforming Data.')
        
        labels = ['- Converting datetime and date_of_birth to datetime objects and transforming them to the pattern mm/dd/yyyy',
                  '- Filling NA.',
                  '- Creating ID for Outcome type and Outcome Event Type.',
                  '- Correcting Column names.']
        
        print(labels[0])

        # data['datetime'] = pd.to_datetime(data['datetime']).dt.strftime('%d-%m-%Y')
        # data['date_of_birth'] = pd.to_datetime(data['date_of_birth']).dt.strftime('%d-%m-%Y')

        print(labels[1])

        data.fillna('Not Recorded',inplace=True)

        print(labels[2])

        data['Outcome_Type_ID'] = data.index + 1
        data['Outcome_Event_ID'] = data.index + 1

        print(labels[3])

        # Dividing into entities 
        animal_table = ['animal_id', 'breed', 'color', 'name','date_of_birth','animal_type']
        outcome_table = ['Outcome_Type_ID','outcome_type']
        outcome_event = ['Outcome_Type_ID','datetime','sex_upon_outcome','outcome_subtype','animal_id',]
        data_colums_order = ['animal_id','breed','color',
               'name','date_of_birth','animal_type','datetime',
               'sex_upon_outcome','outcome_subtype',
               'Outcome_Type_ID','Outcome_Event_ID','outcome_type']

        # re-ordering
        data = data[data_colums_order]
        animal = data[animal_table]
        outcomes = data[outcome_table]
        outcome_events = data[outcome_event]

        # correcting column names

        animal_sql_cols =[
            'Animal_ID',
            'Breed',
            'Color',
            'Name',
            'Date_of_Birth',
            'Animal_Type'
        ]

        outcome_sql_cols = [
            'Outcome_Type_ID',
            'Outcome_Type'
        ]

        outcomeevents_sql_cols = [
            'Outcome_Event_ID',
            'DateTime',
            'Sex_upon_Outcome',
            'Outcome_Subtype',
            'Animal_ID',
        ]

        fact_table_columns = [
            'Animal_ID',
            'Breed',
            'Color',
            'Name',
            'Date_of_Birth',
            'Animal_Type',
            'DateTime',
            'Sex_upon_Outcome',
            'Outcome_Subtype',
            'Outcome_Type_ID',
            'Outcome_Event_ID',
            'Outcome_Type'
        ]

        animal_sql_cols = [column.lower() for column in animal_sql_cols]
        outcome_sql_cols = [column.lower() for column in outcome_sql_cols]
        outcomeevents_sql_cols = [column.lower() for column in outcomeevents_sql_cols]
        fact_table_columns = [column.lower() for column in fact_table_columns]



        animal.columns = animal_sql_cols
        outcomes.columns = outcome_sql_cols
        outcome_events.columns = outcomeevents_sql_cols
        data.columns = fact_table_columns


        # Correcting Duplication
        animal.drop_duplicates(inplace=True)
        outcomes.drop_duplicates(inplace=True)
        outcome_events.drop_duplicates(inplace=True)
        data.drop_duplicates(inplace=True)


        outcomes = pd.DataFrame(pd.Series(outcomes['outcome_type'].unique(),name='outcome_type'))
        outcomes['outcome_type_id'] = outcomes.index + 1 
        outcomes = outcomes[['outcome_type_id','outcome_type']]
        



        


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

    # etl_obj
    etl_obj = etl(condition='test')

    data = etl_obj.extract()
    transformed_data = etl_obj.transform(data) # returns transformed 

    #print([df.head(2) for df in transformed_data[1:]])

    etl_obj.load(transformed_data) # takes transformed data



