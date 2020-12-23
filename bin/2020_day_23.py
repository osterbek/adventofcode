def move(cups):
    length = len(cups)
    pick_up = cups[1:4].copy()
    destination = cups[0] - 1
    while destination in pick_up or destination == 0:
        destination -= 1
        if destination < min(cups):
            destination = max(cups)
    cups.extend(cups[0:4])
    del cups[0:4]
    cups = (cups.copy()[:cups.index(destination) + 1] + pick_up.copy() + cups.copy()[cups.index(destination) + 1:])[:length]
    return cups


if __name__ == '__main__':
    cups = [int(i) for i in '614752839']
    for r in range(0, 100):
        cups = move(cups)
    answer_1 = int(str(cups[cups.index(1) + 1:] + cups[:cups.index(1)]).replace(', ', '')[1:-1])
    print('Answer part 1 = {:d} '.format(answer_1), answer_1 == 89372645)
    cups = [int(i) for i in '614752839']
    for i in range(10, 1000000 + 1):
        cups.append(i)
    for r in range(0, 10000000):
        cups = move(cups)
    answer_2 = (cups[cups.index(1) + 1:] + cups[:cups.index(1)])[:2]
    print('Answer part 2 = {:d} '.format(int(answer_2[0]) * int(answer_2[1])))
