import json
import re

with open('chewing_table.vim') as s:
    symbols = set(json.loads(s.read()))

with open('cat.txt', 'w') as txt:
    with open('dict-cat.json') as f:
        cats = json.loads(f.read())
        for cat in cats:
            for entry in cat['entries']:
                entry = re.sub(r'[（(].*$', '', entry)
                if len(entry) == 1 or any(map(lambda x: x not in symbols, entry)):
                    print(entry)
                    continue

                txt.write(entry +'\n')
