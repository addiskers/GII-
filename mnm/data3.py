import json
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')  
db = client['MnMdata'] 
collection = db['structured_headings']  

# File path to the JSON file
file_path = r"C:\Users\admin\Desktop\SQ\MnMdata\filtered_headings.json"

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Function to structure the data into chapters and sub-sections
def structure_data(data):
    structured_data = {}
    for item in data:
        parts = item.split(" ")
        chapter = parts[0].split(".")[0]

        if chapter not in structured_data:
            structured_data[chapter] = {"chapter": item, "sub_sections": []}
        else:
            structured_data[chapter]["sub_sections"].append(item)

    return structured_data

# Structure the data
structured_data = structure_data(data)

# Prepare the document to be inserted
document = {"chapters": []}
for chapter, content in structured_data.items():
    document["chapters"].append({
        "chapter": content["chapter"],
        "sub_sections": content["sub_sections"]
    })

# Insert the document into MongoDB
collection.insert_one(document)
print("Data inserted successfully into MongoDB")

# Verify insertion
inserted_doc = collection.find_one()
print(inserted_doc)
