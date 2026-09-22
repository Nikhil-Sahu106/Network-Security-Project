import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

ca = certifi.where()


class NetworkSecurityData:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            self.db = self.client["NetworkSecurity"]
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def cv_to_json(self, file_path):
        try:
            data = pd.read_csv( file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def insert_data(self, records, database_name, collection_name):
        try:
            self.database_name = database_name
            self.collection_name = collection_name
            self.records = records


            self.mongo_cilent = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_cilent[self.database_name]

            self.collection = self.database[self.collection_name]
            self.collection.insert_many(self.records)
            return (len(self.records))

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    FILE_PATH ="Network_Data\phisingData.csv"
    DATABASE_NAME = "NIKHILdb"
    COLLECTION_NAME = "NetworkData"
    networksecurity_data = NetworkSecurityData()
    records = networksecurity_data.cv_to_json(FILE_PATH)
    no_of_records = networksecurity_data.insert_data(records, DATABASE_NAME, COLLECTION_NAME)
    print(records)
    print(f"Total number of records inserted in the database: {no_of_records}")

    