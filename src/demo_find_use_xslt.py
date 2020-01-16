from pymongo import MongoClient

import lxml.etree as ET
import yaml
import src.xml_utils as UTILS
from src.database import MongoDatabase

with open('database.yaml') as yaml_file:
    config = yaml.safe_load(yaml_file)

mongo_client = MongoClient(config['mongo']['host'], config['mongo']['port'])

db = mongo_client[config['mongo']['database']]
collection = db[config['mongo']['collection']]

db2 = MongoDatabase(config['mongo']['host'], config['mongo']['port'])
collection2 = db2.get_mongo_collection(config['mongo']['database'], config['mongo']['collection'])

documents = collection2.find(
    {'Context.InteractionGroupID': '20200105'},
    {
        '_id': False,
        'FinancialAccountNumber': False,
        'Context': False,
        'TransactionStatus': False
    }
)

customers = UTILS.convert_dictionaries_to_xml_tree(documents, root_name='Customers', element_name='Customer')

print(ET.dump(customers))

customers.write(open('output/output.xml', 'wb'))


UTILS.transform_xml_file_with_xslt('output/output.xml', 'output/transform.xslt', 'output/transformed_file.xml')
