import utils


def build_mapping_file():
    with open('McBopomofo/phrase.occ') as f:
        freq = {}
        for line in f:
            line = line.strip().split()
            freq[line[0]] = int(line[1])

    with open('McBopomofo/BPMFBase.txt') as f:
        for line in f:
            line = line.strip().split()
            if line[0] == line[1]:
                continue

            print('{} {} {}'.format(freq.get(line[0], 0), line[0], line[3]))

    with open('McBopomofo/BPMFMappings.txt') as f:
        for line in f:
            line = line.strip().split()
            symbol_str = ''.join(line[1:])
            print('{} {} {}'.format(
                    freq.get(line[0], 0),
                    line[0],
                    ' '.join(utils.symbol_str_2_code_list(symbol_str))))

if __name__ == '__main__':
    build_mapping_file()
