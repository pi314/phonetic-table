import tr
import code_comb
import re


def symbol_str_2_code_list(symbol_str):
    '''
    >>> symbol_str_2_code_list('')
    []
    >>> symbol_str_2_code_list('ㄘㄜˋ')
    ['hk4']
    >>> symbol_str_2_code_list('ㄘㄜˋㄕˋ')
    ['hk4', 'g4']
    >>> symbol_str_2_code_list('ㄕㄘㄜˋ')
    ['g', 'hk4']
    >>> symbol_str_2_code_list('ㄕㄘˋㄜ')
    ['g', 'h4', 'k']
    >>> symbol_str_2_code_list('ㄘㄜˋㄕˋㄓㄨㄥ ㄨㄣˊ')
    ['hk4', 'g4', '5j/ ', 'jp6']
    >>> symbol_str_2_code_list('ㄉㄨ')
    ['2j']
    >>> symbol_str_2_code_list('ㄨㄉ')
    ['j', '2']
    >>> symbol_str_2_code_list('ㄓㄧ')
    ['5', 'u']
    >>> symbol_str_2_code_list('ㄦㄦㄦ')
    ['-', '-', '-']
    >>> symbol_str_2_code_list('ㄧㄉㄧㄥㄉㄧㄢˇㄦˊ')
    ['u', '2u/', '2u03', '-6']
    >>> symbol_str_2_code_list('ㄧㄒㄧㄝ')
    ['u', 'vu,']
    '''
    if symbol_str == '':
        return []

    if not re.match(r'^[0-9a-z,./;-]$', symbol_str):
        code_str = tr.tr(symbol_str)

    ret = []
    acc = ''
    sound = False
    probe = code_comb.tree
    for c in code_str:
        if c not in probe:
            if c in '3467 ' and not sound:
                acc += c
                probe = {}
                sound = True
            else:
                ret.append(acc)
                acc = c
                probe = code_comb.tree[c]
                sound = False

        else:
            acc += c
            probe = probe[c]

    ret.append(acc)
    return ret
