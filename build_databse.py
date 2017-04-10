tree = {}
record_count = 0

def add_word(tree, code_list, word, freq):
    if code_list[0][-1] not in '3467':
        code_list[0] += ' '

    if len(code_list) == 1:
        pass


with open('output/mapping.txt') as f:
    for line in f:
        line = line.strip().split()
        freq = int(line[0])
        word = line[1]
        code_list = line[2:]
        add_word(tree, code_list, word, freq)
        record_count += 1
