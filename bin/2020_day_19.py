from pathlib import Path
import re


def go_deep(node, depth):
    output = ''
    if depth < 32:
        for item in [i for i in rules.get(node).split(' ')]:
            if item in 'ab|':
                output += item
            else:
                output += '(' + go_deep(int(item), depth + 1) + ')'
    return output


if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_19.txt').read_text().split('\n\n')]
    rules = {}
    for r in [i for i in dataset[0].split('\n')]:
        rules[int(r[:r.find(':')])] = r[r.find(':')+2:].replace('"', '')
    regex_1 = go_deep(0, 0)
    print('Answer part 1 = {:d} '.format(sum([bool(re.fullmatch(regex_1, i)) for i in dataset[1].split('\n')])), 216)
    rules[8] = '42 | 42 8'
    rules[11] = '42 31 | 42 11 31'
    regex_2 = go_deep(0, 0)
    print('Answer part 2 = {:d} '.format(sum([bool(re.fullmatch(regex_2, i)) for i in dataset[1].split('\n')])), 400)
    
