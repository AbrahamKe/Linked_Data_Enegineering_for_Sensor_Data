import json
#import numpy as np
import schedule
from transformation import transformation
class Engine:
	def__init__(self,datasource,dataset):
	data_calculation=Transformation(datasource,dataset)
if__name__=='__main__':
    rdfetl_data=json.load(open('data_config.json'))
    for datasource,dataset in rdfetl_data ['data_sources'].item():
    	print (datasource)
    	for data in dataset:
    		print (data)
    		main_source=Engine(datasource,data)