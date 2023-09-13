import pandas as pd 
import argparse
import time


# reads data from the cloud 

def extract_data():
    return pd.read_csv('https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/people/people-1000.csv')


def transformed(data):

    # Transforms the data birth into 3 separate columns day month and year and drops userid
    print("Transformation")
    print('- Dropping redundancies')
    data = data.drop('User Id',axis=1)
        
    # datetime conversion
    print("- Converting to Datetime objects")
    data['Date of birth'] = pd.to_datetime(data['Date of birth'])
    

    print("- Individualising Month, Day and Year to different columns")
    data['month'] = data['Date of birth'].dt.month
    data['year'] = data['Date of birth'].dt.year
    data['day'] = data['Date of birth'].dt.day


    # saving transformed dataset.
    time.sleep(1)
    print('- Transformation Done!')
    print('- Saving Transformed data. transformed data is saved as /app/transformed-data.csv.')
    
    # try except to handle testing in the host environment
    try:
        data.to_csv('/app/transformed-data.csv',index=False)
    except OSError:
        print()
        print("Oh! We're in the Host Environment!, saving locally as transformed-data.csv")
        data.to_csv('transformed-data.csv',index=False) 

    # data.to_csv('transformed-data.csv',index=False)
    # print("- Modified data is saved as transformed-data.csv")


# prints head of data
def show_data():
    
    data = extract_data()
    print(data.head(10))

def main(read_flag, transformation):
    # calls all the required functions

    if read_flag and transformation:
        
        data = extract_data()

        transformed(data)

    else:

        print('No functionality detected. do python data-pipeline.py --help for manual.')



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process a CSV file with transformations and save the results.")
    parser.add_argument("--read", help="Reads csv file source from the terminal")
    parser.add_argument("--transform", help="Transformation option (example/custom)")
    

    # Parse the command line arguments
    args = parser.parse_args()

    if any(vars(args).values()):
        
        main(args.read, args.transform)
        
        print('-'*55)
        print('Job Completed.')
        print()

    else:
        print('No functionality detected. do python data-pipeline.py --help for manual.')
