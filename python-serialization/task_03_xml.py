#!/usr/bin/python3
"""XML alternative for JSON"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize dictionary to XML file"""

    root = ET.Element("data")

    for key, val in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(val)

    arbol = ET.ElementTree(root)
    arbol.write(filename)


def deserialize_from_xml(filename):
    """deserialize XML to a dictionary"""

    arbol = ET.parse(filename)
    root = arbol.getroot()

    diccionario = {}
    for child in root:
        diccionario[child.tag] = child.text

    return diccionario
