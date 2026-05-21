import numpy as np
import pandas as pd
import os
from  src.logger import logging
from src.custom_exception import customException
import sys
from dataclasses import dataclass

@dataclass
class Datainjestionconfig():
    raw_data_path: str = os.path.join('artifacts','raw_data.csv') 
    train_data_path: str = os.path.join('artifacts','train_data.csv') 
    test_data_path: str = os.path.join('artifacts','test_data.csv') 
    
class DataInjestion():
    def __init__(self):
        self.data_injestion_config = Datainjestionconfig()
        
    def initiate_data_injestion(self):
        logging.info("Data injestion method starts")
        try:
            df = pd.read_csv(os.path.join('notebook/data','raw_data.csv'))
            logging.info("Dataset read as pandas dataframe")
            
            os.makedirs(os.path.dirname(self.data_injestion_config.raw_data_path),exist_ok=True)
            
            df.to_csv(self.data_injestion_config.raw_data_path,index=False)
            logging.info("Raw data is saved")
            
            from sklearn.model_selection import train_test_split
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.data_injestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.data_injestion_config.test_data_path,index=False,header=True)
            logging.info("Data injestion is completed")     
            
            return (self.data_injestion_config.train_data_path,self.data_injestion_config.test_data_path)
            
        except Exception as e:
            raise customException(e,sys.exc_info())
        
    