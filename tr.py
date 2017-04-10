symbols = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦˇˋˊ˙'
codes = '1qaz2wsxedcrfv5tgbyhnujm8ik,9ol.0p;/-3467'

symbol_code_map = str.maketrans(
        symbols + codes + ' ',
        codes + symbols + ' ')

code_combinaiton_tree = {}


def tr(symbol_str):
    '''
    >>> tr(symbols)
    '1qaz2wsxedcrfv5tgbyhnujm8ik,9ol.0p;/-3467'
    >>> tr(codes)
    'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦˇˋˊ˙'
    >>> tr('1qaz')
    'ㄅㄆㄇㄈ'
    '''
    return symbol_str.translate(symbol_code_map)
