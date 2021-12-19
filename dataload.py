import pandas as pd
from pymongo import MongoClient
from influxdb_client import InfluxDBClient, Point, 
from influxdb import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from csv import DictReader
   #generic class functions is designed for different data source
class Databasedata:
	#data to and MongoDB
	def__init__(self,user,password,host,db_name,port='27017')
	      self.user= user
	      self.password=password
	      self.port=port 
          self.db_name=mongoosh
          self.uri='mongodb://+self.user+':'+ self.password+'@'+ self.host+ self.port +'/'+self.db_name'

          #connect to the database

          try:
          	self.Client=MongoClient(self.uri)
          	self.db=self.client[self.db_name]
          	print('Connection Successful')

          except Exception as e:
          	print ('Connection Failed')
          	print (e)
     # data dictionary
     def insert_into_mongodatabase(self.data,collection):
     	if isinstance (data,pd.DataFrame):
     		try:
     			self.db [collection].insert_many(data.to_dict('mongoosh'))
     			print ('Data is Inserted')
     		except Exception as e:
     			print ('Insertion Failed')
     			print (e)
     		else:
     			try:
     				self.db[collection].insert_many(data)
     				print ('Data is Inserted')
     			except Exception as e:
     				print ('Insertion Failed')
     				print (e)
     def Load_from_mongodbs(self, collection):
     	try:
     		data=pd.DataFrame(list(self.db[collection].find()))
     		print ('Data is Retrived')
     		return Data
     	except Exception as e:
     		print ('Error, try again')
     		print (e)

      #data to and from Influxdb
     def__init__(self,user,password,host,db_name,port= '8086')
	      self.user= user
	      self.password=password
	      self.port=port 
          self.db_name=influxdbosh
          self.uri='influxdb://+self.user+':'+ self.password+'@'+ self.host+ self.port +'/'+self.db_name'
          try:
          	self.Client=InfluxDBClient(self.uri)
          	self.db=self.client[self.db_name]
          	print('Connection Successful')

          except Exception as e:
          	print ('Connection Failed')
          	print (e)

      def insert_into_influxdatabase(self.data, data):

     		data = []
      data.append("{measurement},sensor={temprature_sensor},sensorvalue={value}, {unix_timestamp}"
            .format(measurement=temprature,
                    sensor=temprature_sensor,
                    sensorvalue=value,               
                                    
                    timestamp=data_start_time))
     client.write_points(data, database='influxdb_OSH', protocol='line')