from pathlib import Path


def dissolve_parenthesis(term, part):
    term = term.split(' ')
    if part == 2:
        while '+' in term:
            term[term.index('+') - 1] = int(term[term.index('+') - 1]) + int(term[term.index('+') + 1])
            del term[term.index('+') + 1]
            term.remove('+')
    result = int(term[0])
    for i in range(1, len(term)-1, 2):
        if term[i] == '+':
            result += int(term[i + 1])
        else:
            result *= int(term[i + 1])
    return result


def evaluate_expression(line, part):
    while ')' in line:
        b = line.index(')')
        a = line[:b].rfind('(')
        line = line[:a] + str(dissolve_parenthesis(line[a+1:b], part)) + line[b+1:]
    return dissolve_parenthesis(line, part)


if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_18.txt').read_text().split('\n')]
    answer_1 = 0
    answer_2 = 0
    for entry in dataset:
        answer_1 += evaluate_expression(entry, 1)
        answer_2 += evaluate_expression(entry, 2)
    print('Answer part 1 = {:d} '.format(answer_1), answer_1 == 5374004645253)
    print('Answer part 2 = {:d} '.format(answer_2), answer_2 == 88782789402798)
    
