import pymongo 
import pandas as pd
import json
from pymongo.mongo_client import MongoClient

client = pymongo.MongoClient("mongodb+srv://Amit8281:Amit8281@cluster0.jwsyedo.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"D:\DATA_SCIENCE_PROJECT\INSURANCE_PRICE\insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"rows and column",df.shape)


    df.reset_index(drop=True,inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)