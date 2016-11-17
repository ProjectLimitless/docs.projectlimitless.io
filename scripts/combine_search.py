import os
import os.path
import json

print('Combining multiple search indexes')

items = []

for dirpath, dirnames, filenames in os.walk("./out"):
    for filename in [f for f in filenames if f.endswith("search_index.json")]:
        json_file = os.path.join(dirpath, filename)
        if json_file == './out/mkdocs/search_index.json':
            continue
        with open(json_file) as json_data:
            d = json.load(json_data)
            for item in d['docs']:
                #print(item['title')
                items.append(item)

doc = {
    'docs': items
}
with open('./out/mkdocs/search_index.json', 'w') as outfile:
    json.dump(doc, outfile)
print('Combined a total of %d items' % len(items))
