zhuyin_symbols = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦˇˋˊ˙'
zhuyin_codes = '1qaz2wsxedcrfv5tgbyhnujm8ik,9ol.0p;/-3467'
code_symbol_trans = str.maketrans(zhuyin_symbols, zhuyin_codes)

def zhuyin2code(x):
    return x.translate(code_symbol_trans)

pinyin2zhuyin_table = {}

with open('zhuyin-pinyin-ipa-table') as f:
    for line in f:
        a, b, _ = line.split()
        pinyin2zhuyin_table[b] = zhuyin2code(a)

for key in sorted(pinyin2zhuyin_table.keys()):
    print("let s:pinyin_comb['{}'] = '{}'".format(key, pinyin2zhuyin_table[key]))
