# -*- coding: utf-8 -*-
import unittest
from paige_assignment import transformation


class Transform_Test(unittest.TestCase):
    
    
    #test to verify if the data loads correctly 
      def setUp(self):
        self.testdata = open(patient_data.csv).read()
        
        
    
    # test for missing values
      def test_missing_value(self):
         assert df['glucose_mg/dl_t1'].isna().sum()<1
         assert df['glucose_mg/dl_t2'].isna().sum()<1
         assert df['Average'].isna().sum()<1
         
            
       # test for the shape     
      def test_shape(self):       
        assert df['id'].unique().shape[0] == len(ids)
       # function returns have shapes as expected
        assert all([DiabetiesDataClean(df).shape == df[0].shape for df in dfs])
        
        
    
     
    # test to verify if the data is of the desired instance 
      def test_data(self):
        data= getCSVData():
        assert all(data.columns==['patient_id','glucose_mg/dl_t1','glucose_mg/dl_t2','glucose_mg/dl_t3','Average'])
        assert isinstance(datacolumns==int)  
    
    
    
    # Test to find the expected average
      def test_average_glucose_level(self):
        
        data= getCSVData()
        expected={0:3,1:4}
        result=DiabetiesDataClean(data,"Average")
        assert expected== result
        
            
if __name__ == '__main__':
    unittest.main()

