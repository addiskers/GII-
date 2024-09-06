from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/') 
db = client['MnMdata']  
collection = db['structured_headings']  


document = collection.find_one()


if document:

    for i in document.get('chapters', []):
       if "BY" in i['chapter'] and "REGION" not in i['chapter'] or "COMPANY" in i["chapter"]:
            print(f"Chapter: {i['chapter']}")
            for subsection in i['sub_sections']:
                print(f"- {subsection}")
else:
    print("No document found.")

