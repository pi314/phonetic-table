import json
import re
import charset

with open('revised.txt', 'w') as txt:
    with open('dict-revised.json') as f:
        entries = json.loads(f.read())
        for entry in entries:
            entry['title'] = re.sub(r'[（(].*$', '', entry['title'])
            if len(entry['title']) == 1 or any(map(lambda x: x not in charset.table, entry['title'])):
                print(entry['title'])
                continue

            txt.write('{} {}\n'.format(entry['title'], entry['heteronyms'][0]['bopomofo']))
