from pathlib import Path


if __name__ == '__main__':
    cups = [int(i) for i in Path('../input/input_2020_23.txt').read_text()]
    for r in range(0, 100):
        pick_up = cups[1:4].copy()
        destination = cups[0] - 1
        while destination in pick_up or destination == 0:
            destination -= 1
            if destination < min(cups):
                destination = max(cups)
        cups.extend(cups)
        del cups[0:4]
        cups = (cups.copy()[:cups.index(destination)+1] + pick_up.copy() + cups.copy()[cups.index(destination)+1:])[:9]
    answer_1 = int(str(cups[cups.index(1) + 1:] + cups[:cups.index(1)]).replace(', ', '')[1:-1])
    print('Answer part 1 = {:d} '.format(answer_1), answer_1 == 89372645)
