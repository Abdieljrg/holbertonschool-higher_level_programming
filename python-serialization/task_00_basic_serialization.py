#!/usr/bin/python3
""" basic serialization """
import json


def serialize_and_save_to_file(data, filename):
    """serializing the file"""
    with open (filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """loading the file"""
    with open (filename, 'r') as file:
        load_file = json.load(file)
    return (load_file)
