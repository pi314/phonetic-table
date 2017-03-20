cat_table = set()
revised_table = set()

with open('cat.txt') as f:
    for line in f:
        cat_table.add(line.strip())

with open('revised.txt') as f:
    for line in f:
        revised_table.add(line.strip().split()[0])

for word in cat_table:
    if word not in revised_table:
        print(word)
