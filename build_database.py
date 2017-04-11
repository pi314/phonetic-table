import tr


tree = {}
record_count = 0

def add_word(tree, code_list, word, freq):
    if code_list[0][-1] not in '3467':
        code_list[0] += ' '

    if len(code_list) == 1:
        if code_list[0] not in tree:
            tree[code_list[0]] = [{'w': word, 'f': freq}]
        elif isinstance(tree[code_list[0]], dict):
            if '_' in tree[code_list[0]]:
                tree[code_list[0]]['_'].append({'w': word, 'f': freq})
                tree[code_list[0]]['_'].sort(key=lambda x: x['f'], reverse=True)
            else:
                tree[code_list[0]]['_'] = [{'w': word, 'f': freq}]
        elif isinstance(tree[code_list[0]], list):
            tree[code_list[0]].append({'w': word, 'f': freq})
            tree[code_list[0]].sort(key=lambda x: x['f'], reverse=True)
    else:
        if code_list[0] not in tree:
            tree[code_list[0]] = {}

        if isinstance(tree[code_list[0]], dict):
            add_word(tree[code_list[0]], code_list[1:], word, freq)

        elif isinstance(tree[code_list[0]], list):
            tmp = tree[code_list[0]]
            tree[code_list[0]] = {}
            tree[code_list[0]]['_'] = tmp
            add_word(tree[code_list[0]], code_list[1:], word, freq)


with open('output/mapping.txt') as f:
    for line in f:
        line = line.strip().split()
        freq = int(line[0])
        word = line[1]
        code_list = line[2:]
        add_word(tree, code_list, word, freq)
        record_count += 1


def gen_vim_code(tree=tree, prefix='let s:table'):
    print('{} = {{}}'.format(prefix))
    if '_' in tree:
        print('{}[\'_\'] = {}'.format(prefix, tree['_']))

    for k in sorted(filter(lambda x: x != '_', tree.keys())):
        if isinstance(tree[k], list):
            print('{}[\'{}\'] = {}'.format(prefix, k, tree[k]))
        else:
            gen_vim_code(tree[k], '{}[\'{}\']'.format(prefix, k))


if __name__ == '__main__':
    gen_vim_code()
