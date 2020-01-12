from pymongo import MongoClient
from pprint import pprint

import dicttoxml
from xmltodict import unparse
import yaml

with open('database.yaml') as yaml_file:
    config = yaml.safe_load(yaml_file)

mongo_client = MongoClient(config['mongo']['host'], config['mongo']['port'])

db = mongo_client[config['mongo']['database']]
collection = db[config['mongo']['collection']]

obj = collection.find_one({'Context.InteractionGroupID': '20200105'}, {'_id': False, 'FinancialAccountNumber': False, 'Context': False, 'TransactionStatus': False})

print(type(obj))
pprint(obj)

xml = dicttoxml(obj)
xml_string = str(xml)
xml_string_2 = unparse({"Document": obj})

print(type(xml_string))
print(xml_string)

print(type(xml))
pprint(xml)

print(type(xml_string_2))
print(xml_string_2)

with open("output/output.xml", "w") as f:
    f.write(xml_string_2)


