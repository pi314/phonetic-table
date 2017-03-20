import re
import json

import jieba

import symbol2code
import code2char


table = {}

def add_word(t, word, codes):
    # print(word, codes)
    if len(codes) == 0:
        if '' not in t:
            t[''] = []
        if word not in t['']:
            t[''] += [word]

    else:
        if codes[0] not in t:
            t[codes[0]] = {}
        add_word(t[codes[0]], word, codes[1:])


for code in code2char.table:
    table[code] = {}
    table[code][''] = code2char.table[code]


with open('combine.txt') as f:
    for line in f:
        line = line.strip().split(' ')
        line[1] = list(map(lambda x: symbol2code.tr(x), re.split(r'（.*）', line[1])))
        line[1] = list(map(lambda x: x.split(), line[1]))
        line[1] = list(map(lambda y: list(map(lambda x: x + ' ' if re.match(r'.*[^3467]$', x) else x, y)), line[1]))

        for word in jieba.cut(line[0]):
            if len(word) > 1:
                for word_code in line[1]:
                    if len(word_code[line[0].index(word): line[0].index(word) + len(word)]) == 0:
                        print(line[0], word, word_code)
                        assert False
                    add_word(table, word, word_code[line[0].index(word): line[0].index(word) + len(word)])


print(json.dumps(table))
