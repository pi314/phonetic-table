import phonetic_table

zhuyin_codes = '1qaz2wsxedcrfv5tgbyhnujm8ik,9ol.0p;/-3467'
zhuyin_symbols = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦˇˋˊ˙'
code_symbol_trans = str.maketrans(zhuyin_codes, zhuyin_symbols)

def code2zhuyin(x):
    return x.translate(code_symbol_trans)

zhuyin2ipa_table = {}

with open('zhuyin-pinyin-ipa-table') as f:
    for line in f:
        a, _, b = line.split()
        zhuyin2ipa_table[a] = b
        zhuyin2ipa_table[a + ' '] = b + '55'
        zhuyin2ipa_table[a + 'ˊ'] = b + '35'
        zhuyin2ipa_table[a + 'ˇ'] = b + '214'
        zhuyin2ipa_table[a + 'ˋ'] = b + '51'
        zhuyin2ipa_table[a + '˙'] = b

def zhuyin2ipa(x):
    return zhuyin2ipa_table[x]


def code2ipa(x):
    return '_' if x == '_' else zhuyin2ipa(code2zhuyin(x))


res = set()

def recursive_collect_key(res, table):
    for key in table.keys():
        res.add(code2zhuyin(key))
        if isinstance(table[key], dict):
            recursive_collect_key(res, table[key])

recursive_collect_key(res, phonetic_table.table)


print('let s:table = {}')
for key, value in sorted(zhuyin2ipa_table.items()):
    if key in res:
        print("let s:table['{}'] = '{}'".format(key, value))
