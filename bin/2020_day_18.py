from pathlib import Path


def dissolve_parenthesis(term, part):
    term = term.split(' ')
    for i in range(0, len(term)):
        if (term[i] != '+') and (term[i] != '*'):
            term[i] = int(term[i])
    if part == 1:
        result = int(term[0])
        for i in range(1, len(term)-1, 2):
            if term[i] == '+':
                result += term[i+1]
            else:
                result *= term[i + 1]
    else:
        while '+' in term:
            term[term.index('+') - 1] += term[term.index('+') + 1]
            del term[term.index('+') + 1]
            term.remove('+')
        result = 1
        for i in range(0, len(term), 2):
            result *= term[i]
    return result


def evaluate_expression(line, part):
    sth_changed = True
    while sth_changed:
        i = 0
        position = 0
        sth_changed = False
        while i < len(line):
            if line[i] == '(':
                position = i
            if line[i] == ')':
                line = line[:position] + str(dissolve_parenthesis(line[position + 1:i], part)) + line[i + 1:]
                sth_changed = True
                break
            i += 1
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
