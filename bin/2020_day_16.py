from pathlib import Path


if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_16.txt').read_text().split('\n\n')]
    rules = []
    for r in [j for j in dataset[0].split('\n')]:
        a = r.split(':')[1].split(' or ')
        b = a[0].split('-')
        c = a[1].split('-')
        rules.append([r.split(':')[0], int(b[0]), int(b[1]), int(c[0]), int(c[1])])
    yours = [int(j) for j in [i for i in dataset[1].split('\n')][1].split(',')]
    nearby = []
    for n in [i for i in dataset[2].split('\n')]:
        if 'nearby' not in n:
            nearby.append([int(j) for j in [i for i in n.split(',')]])

    answer_1 = 0
    tickets = []
    for ticket in nearby:
        ticket_valid = True
        for value in ticket:
            valid = False
            for rule in rules:
                if ((value >= rule[1]) and (value <= rule[2])) or ((value >= rule[3]) and (value <= rule[4])):
                    valid = True
            if not valid:
                answer_1 += value
                ticket_valid = False
        if ticket_valid:
            tickets.append(ticket)
    print('Answer part 1 = {:d} '.format(answer_1), answer_1 == 25916)

    p = [[1 for j in rules] for i in rules]
    for x in range(0, len(rules)):
        for t in tickets:
            for y in range(0, len(t)):
                if ((t[y] < rules[x][1]) or (t[y] > rules[x][2])) and ((t[y] < rules[x][3]) or (t[y] > rules[x][4])):
                    p[y][x] = 0
    x = 0
    while sum([sum(i) for i in p]) > len(rules):
        if sum(p[x]) == 1:
            for y in range(0, len(rules)):
                if y != x:
                    p[y][p[x].index(1)] = 0
        x += 1
        if x >= len(rules):
            x = 0
    answer_2 = 1
    for y in range(0, len(rules)):
        for x in range(0, len(rules)):
            if p[y][x] == 1:
                if rules[x][0][:9] == 'departure':
                    answer_2 = answer_2 * yours[y]
    print('Answer part 2 = {:d} '.format(answer_2), answer_2 == 2564529489989)
