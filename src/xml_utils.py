import lxml.etree as ET
import json


def validate_xml_file_with_xsd(xml_filename, xsd_filename):
    xsd_file_tree = ET.parse(xsd_filename)
    xml_filename = ET.parse(xml_filename)
    xml_schema = ET.XMLSchema(xsd_file_tree)


def transform_xml_file_with_xslt(xml_filename, xslt_filename, output_filename, encoding='UTF-8'):
    original_xml_tree = ET.parse(xml_filename)
    xslt_tree = ET.parse(xslt_filename)
    transform = ET.XSLT(xslt_tree)
    transformed_xml_tree = transform(original_xml_tree)
    transformed_xml_tree.write(open(output_filename), 'wb', encoding=encoding)


def load_json_file_to_dictionaries(filename):
    with open(filename) as f:
        dictionaries = json.load(f)
    return dictionaries


def convert_dictionaries_to_xml_tree(dictionaries, root_name, element_name):
    root = ET.Element(root_name)

    for dictionary in dictionaries:
        for key in dictionary:
            if dictionary[key] is None:
                text_value = 'null'
            else:
                text_value = dictionary[key]
            temp = ET.SubElement(element_name, key)
            temp.text = text_value

    return ET(root)

