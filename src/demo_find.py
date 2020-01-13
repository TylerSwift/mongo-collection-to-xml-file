from pymongo import MongoClient

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree
import yaml

with open('database.yaml') as yaml_file:
    config = yaml.safe_load(yaml_file)

mongo_client = MongoClient(config['mongo']['host'], config['mongo']['port'])

db = mongo_client[config['mongo']['database']]
collection = db[config['mongo']['collection']]

documents = collection.find(
    {'Context.InteractionGroupID': '20200105'},
    {
        '_id': False,
        'FinancialAccountNumber': False,
        'Context': False,
        'TransactionStatus': False
    }
)

customers = ET.Element('Customers')

for doc in documents:
    customer = ET.SubElement(customers, 'Customer')
    for key in doc:
        temp = ET.SubElement(customer, key)
        temp.text = doc[key]

print(ET.dump(customers))

tree = ElementTree(customers)
tree.write(open('output/output.xml', 'wb'))
