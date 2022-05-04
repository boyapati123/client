"""Routines associated with the application data.
"""
import json
import os



courses = {}

def load_data():
    with open(os.path.abspath("json")+'/course.json','r') as f:
        return json.load(f)

def save_data(json_data):
    with open(os.path.abspath("json")+'/titanic.json', 'w') as f:
        json.dump(json_data, f, indent=4)

if __name__ == '__main__':
    print(load_data())