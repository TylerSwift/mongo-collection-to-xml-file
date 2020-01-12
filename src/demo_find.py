from pymongo import MongoClient
from pprint import pprint
from dicttoxml import dicttoxml
from xmltodict import unparse
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

# xml = dicttoxml(obj)
# xml_string = str(xml)
# xml_string_2 = unparse({"Document": obj})
#
# print(type(xml_string))
# print(xml_string)
#
# print(type(xml))
# pprint(xml)
#
# print(type(xml_string_2))
# print(xml_string_2)

customers = ET.Element('Customers')

for doc in documents:
    customer = ET.SubElement(customers, 'Customer')

    dlr_cd = ET.SubElement(customer, 'DLR_CD')
    dlr_cd.text = doc['DLR_CD']

    db_num = ET.SubElement(customer, 'DB_NM')
    db_num.text = doc['DB_NM']

    lgl_nm = ET.SubElement(customer, 'LGL_NM')
    lgl_nm.text = doc['LGL_NM']

    fed_tax_no = ET.SubElement(customer, 'FED_TAX_NO')
    fed_tax_no.text = doc['FED_TAX_NO']



print(ET.dump(customers))

tree = ElementTree(customers)
tree.write(open('output/output.xml', 'wb'))
