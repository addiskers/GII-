from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  
db = client['MnM']
collection = db['data']


def print_hierarchy(data, level=0):
    for key, value in data.items():
        indent = ' ' * (4 * level)
        if 'content' in value:
            print(f"{indent}{key} {value['content']}")
            if 'subsections' in value and value['subsections']:
                print_hierarchy(value['subsections'], level + 1)
        else:
            
            print(f"{indent}{key}")
            print_hierarchy(value, level + 1)

# Fetch the document from MongoDB
document = collection.find_one()


if '_id' in document:
    del document['_id']

# Print the hierarchy
print_hierarchy(document)

print("Data printed successfully")
