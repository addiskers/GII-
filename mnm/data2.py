import json
import re

# Path to the JSON file
file_path = r'C:\Users\admin\Desktop\SQ\MnMdata\table_of_contents.json'
output_file_path = r'C:\Users\admin\Desktop\SQ\MnMdata\filtered_headings.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

def parse_headings(data):
    headings = {}
    pattern = re.compile(r'^(\d+(\.\d+)*)')  
    
    for entry in data:
        match = pattern.match(entry)
        if match:
            key = match.group(1)
            headings[key] = entry
    
    return headings

def get_sibling_count(heading, headings):
    parts = heading.split('.')
    base = '.'.join(parts[:-1]) if len(parts) > 1 else ''
    count = 0
    for i in range(1, 100):
        sibling = base + '.' + str(i) if base else str(i)
        if sibling in headings:
            count += 1
        if count >= 2:
            return count
    return count

def heading_exists(heading, headings):
    return heading in headings

def should_print(heading, headings):
    sibling_count = get_sibling_count(heading, headings)
    return sibling_count >= 2

def filter_headings(headings):
    filtered = []
    keys = sorted(headings.keys(), key=lambda x: list(map(int, x.split('.'))))
    
    i = 0
    while i < len(keys):
        current = keys[i]
        if should_print(current, headings):
            filtered.append(headings[current])
            # Take all subsequent subheadings
            i += 1
            while i < len(keys) and keys[i].startswith(current + '.'):
                sub_heading = keys[i]
                if should_print(sub_heading, headings):
                    filtered.append(headings[sub_heading])
                i += 1
        else:
            i += 1
    
    return filtered

headings = parse_headings(data)
filtered_headings = filter_headings(headings)

# Write the filtered headings to a new JSON file
with open(output_file_path, 'w') as output_file:
    json.dump(filtered_headings, output_file, indent=4)

print(f"Filtered headings have been saved to {output_file_path}")


