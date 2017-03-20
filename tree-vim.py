import json

with open('tree.json') as f:
    table = json.loads(f.read())


def print_tree(t, prefix):
    if len(t) == 1 and '' in t:
        print('let s:table{} = {}'.format(prefix, t['']))
        return

    print('let s:table{} = {{}}'.format(prefix))

    if '' in t:
        print('let s:table{}[\'\'] = {}'.format(prefix, t['']))

    for code, sub_tree in sorted(t.items()):
        if isinstance(sub_tree, dict):
            print_tree(sub_tree, prefix + "['{}']".format(code))


print_tree(table, '')
