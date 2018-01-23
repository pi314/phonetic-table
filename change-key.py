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


res = {}

def recursive_change_key(dst, src):
    for key in src.keys():
        new_key = code2ipa(key)
        if isinstance(src[key], list):
            dst[new_key] = src[key]
        else:
            dst[new_key] = {}
            recursive_change_key(dst[new_key], src[key])

recursive_change_key(res, phonetic_table.table)
print(code2ipa('-3'))
print(res['əɻ214'])
