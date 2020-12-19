from pathlib import Path
import re


def go_deep(node, depth):
    output = ''
    if depth < 40:
        for item in [i.replace('"', '') for i in rules.get(node).split(' ')]:
            if item in 'ab|':
                output += item
            else:
                output += '(' + go_deep(int(item), depth + 1) + ')'
    return output


if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_19.txt').read_text().split('\n\n')]
    rules = {}
    for r in [i for i in dataset[0].split('\n')]:
        rules[int(r[:r.find(':')])] = r[r.find(':')+2:]
    regex_part_1 = go_deep(0, 0)
    rules[8] = '42 | 42 8'
    rules[11] = '42 31 | 42 11 31'
    regex_part_2 = go_deep(0, 0)
    answer_1 = 0
    answer_2 = 0
    for i in [i for i in dataset[1].split('\n')]:
        answer_1 += bool(re.fullmatch(regex_part_1, i))
        answer_2 += bool(re.fullmatch(regex_part_2, i))
    print('Answer part 1 = {:d} '.format(answer_1), answer_1 == 216)
    print('Answer part 2 = {:d} '.format(answer_2), answer_2 == 400)
