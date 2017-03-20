symbols = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦˇˋˊ˙'
codes = '1qaz2wsxedcrfv5tgbyhnujm8ik,9ol.0p;/-3467'

table = dict(zip(symbols, codes))

table['　'] = ' '
table[' '] = ' '

def tr(word):
    return ''.join([table[s] for s in word]).strip()

# print(tr('ㄖㄣˊ  ㄨˊ  ㄏㄥˋ  ㄘㄞˊ  ㄅㄨˋ  ㄈㄨˋ'))
