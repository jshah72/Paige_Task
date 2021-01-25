# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


data=pd.read_csv("patient_data.csv")
data.head()

data_source = {"csv": "C:/Users/AU003TX/Desktop"}



class Extract:
    def __init__(self):
        self.csv_path = self.data_source['csv']
        
    def getCSVData(self, csv_name):
        # since we can use multiple CSV data files in future, 
        # so will pass csv name as an argument to fetch the desired CSV data.
        # so in our case it is "patient data"
        df = pd.read_csv(self.csv_path[csv_name])
        return df
        





from DataSources import Extract
import urllib



class Transformation:
    
    def __init__(self, dataSource, dataSet):
      
        # creating Extract class object here, to fetch data using its generic methods for  CSV data sources
        extractObj = Extract()
        
        if dataSource == 'csv':
            self.data = extractObj.getCSVData(dataSet)
            funcName = dataSource+dataSet
            getattr(self, funcName)()
        else:
            print('Unkown Data Source!!! Please try again...')
            
            #Remove PHI Step 4
    def DiabetiesDataClean(self):
        self.csv_df.drop(columns=["first_name","lastName","Email","Address"],inplace = True)
        
        # dropping rows with null values by asset column Step 5
        self.csv_df.dropna(inplace=True)
        
        diabeties_columns = ['glucose_mg/dl_t1','glucose_mg/dl_t2','glucose_mg/dl_t3']
        
        
        #Added a column that calculates the average of all three glucose measurements 
        self.csv_df["Average"]= np.round((self.csv_df.loc[:,'glucose_mg/dl_t1':'glucose_mg/dl_t2': 'glucose_mg/dl_t3']).mean(axis=1))
        
        
        self.csv_data = self.csv_df[(self.csv_df['glucose_mg/dl_t1'] & self.csv_df['glucose_mg/dl_t2'] & self.csv_df['glucose_mg/dl_t3'] > 0)]
        
        return self.csv_df


    
    #  Add a column based on the average of all three glucose measurement time points that indicates whether it’s normal, prediabetes or diabetes.
    def diabetic_range_finder(self):
        diabetic_range = []    
        for i in data_copy["diabetic"].values:
            if (i > 200):
                diabetic_range.append("diabetic")
            elif(i < 140):
                diabetic_range.append("normal")
            else:
                diabetic_range.append("prediabetic")
            return data_copy["diabetic value"] = diabetic_range
        
        
        
        
        
        


# Store the data in database

class MongoDB:

    # Initilize the common usable variables in below function:  
    def __init__(self, user, password, host, db_name ,port='27017', authSource='admin'):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.authSource = authSource
        self.uri = 'mongodb://' + self.user + ':' + self.password + '@'+ self.host + ':' + self.port + '/' + self.db_name + '?authSource=' + self.authSource
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            print('MongoDB Connection Successful. CHEERS!!!')
        except Exception as e:
            print('Connection Unsuccessful!! ERROR!!')
            print(e)

    # Function to insert data in DB, could handle Python dictionary and Pandas dataframes
    def insert_into_db(self, data, collection):
        if isinstance(data, pd.DataFrame):
            try:
                self.db[collection].insert_many(data.to_dict('records'))
                print('Data Inserted Successfully')
            except Exception as e:
                print('OOPS!! Some ERROR Occurred')
                print(e)
        else:
            try:
                self.db[collection].insert_many(data)
                print('Data Inserted Successfully')
            except Exception as e:
                print('OOPS!! Some ERROR Occurred')
                print(e)
    
    def read_from_db(self, collection):
        try:
            data = pd.DataFrame(list(self.db[collection].find()))
            print('Data Fetched Successfully')
            return data
        except Exception as e:
            print('OOPS!! Some ERROR Occurred')
            print(e)
            
            
            
    