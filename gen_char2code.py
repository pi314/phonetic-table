import code2char

table = {}
for code in code2char.table:
    for char in code2char.table[code]:
        if char not in table:
            table[char] = []

        table[char] += [code]

print('table = {}')
for char in table:
    print("table['{}'] = {}".format(char, table[char]))
