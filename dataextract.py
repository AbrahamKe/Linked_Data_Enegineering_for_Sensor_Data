

import pandas as pd
import requests   # used for fetching data from RESTAPI
import json
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, 
from influxdb import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from pymongo import MongoClient
from csv import DictReader
# Token generated from "Tokens Tab" in the UI
token = "NThe9UGaRMyAHMJHfi2UyTLiDZ2sCutnUfCpf5EMUIh5OFVBXiJZC2WCJrBsOMNu797Rcm3nZ-KY8NYC3fYqiw=="
org = " "   # Organazation
bucket = "OSH"  # Open Smart Home

client = InfluxDBClient(url="http://localhost:8086", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

data = "mem,host=host1 used_percent=23.43234543"
write_api.write(bucket, org, data)
#write_api.close()

client.create_database(oshdb)  # open smart home database
client.get_list_database()
client.switch_database ('oshdb')
file_path= r'C:\OSH\influxdb\Bathroom_temprature.csv'
csvheader = pd.read.csv(file_path)
print (csvheader.shape)
print (csvReader.columns)

# generic function
class Extract: 
   def __init__(self):
      # load JSON file
      self.data_sources=json.load(open('data_config.json'))
      self.api=self.data_sources['data_sources']['api']
      self.csv_path=self.data_sources['data_sources']['csv']

   def getAPIData (self,api_name):
        api_url=self.api[api_name]
        response=requests.get(api_url) # convert JSON data in to Python dictionary
        return response.json()
        client.write_points(json) # sensor data
   def getCSVData (self)
       dataframe=pd.read_csv(self.csv_path[csv_name])
       return dataframe




