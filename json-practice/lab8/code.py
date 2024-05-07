import json

with open('/workspace/json-practice/data/schacon.repos.json', 'r') as file:
    data = json.load(file)

top_row = data[:5]
for each in top_row:
    with open("chacon.csv","a") as file:
        csl = each['name'] +  ',' + each['html_url'] + ',' + each['updated_at'] + ',' + each['visibility'] + '\n'
        file.write(csl)


