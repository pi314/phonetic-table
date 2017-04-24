import tr


with open('symbol-combinations.txt') as f:
    symbol_combinations = list(map(lambda x: tr.tr(x.strip()), f.readlines()))


tree = {}


def add_code_to_tree(tree, code):
    if code[0] not in tree:
        tree[code[0]] = {}

    if len(code) == 1:
        tree[code[0]]['_'] = 1
    else:
        add_code_to_tree(tree[code[0]], code[1:])

for comb in symbol_combinations:
    add_code_to_tree(tree, comb)


def gen_vim_code(tree=tree, prefix='let s:code_comb'):
    print('{} = {{}}'.format(prefix))
    if '_' in tree:
        print('{}[\'_\'] = 1'.format(prefix))

    for k in sorted(filter(lambda x: x != '_', tree.keys()), key=lambda x: tr.codes.index(x)):
        if tree[k] == 1:
            print('{}[\'{}\'] = 1'.format(prefix, k))
        else:
            gen_vim_code(tree[k], '{}[\'{}\']'.format(prefix, k))


if __name__ == '__main__':
    gen_vim_code()
