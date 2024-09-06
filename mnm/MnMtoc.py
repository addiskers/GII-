import json
from pymongo import MongoClient

# Load JSON data
with open(r'C:\Users\admin\Desktop\SQ\ccus_absorption\table_of_contents.json', 'r') as file:
    data = json.load(file)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  
db = client['MnM']
collection = db['data']

# Function to build hierarchy
def build_hierarchy(data):
    hierarchy = {}
    
    for item in data:
        parts = item.split(' ', 1)
        key = parts[0]
        content = parts[1] if len(parts) > 1 else ""
        
        levels = key.split('.')
        current_level = hierarchy
        
        for level in levels[:-1]:
            if level not in current_level:
                current_level[level] = {'content': '', 'subsections': {}}
            current_level = current_level[level]['subsections']
        
        current_level[levels[-1]] = {
            'content': content,
            'subsections': {}
        }
    
    return hierarchy

# Insert data into MongoDB
hierarchy = build_hierarchy(data)
collection.insert_one(hierarchy)

print("Data inserted successfully")