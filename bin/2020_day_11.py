from pathlib import Path


def free_direction_count(s, x_0, y_0, adjacent):
    counter = 0
    for direction in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        unwanted = False
        x = x_0
        y = y_0
        while True:
            x += direction[0]
            y += direction[1]
            if (x < 0) or (x >= len(s[0])) or (y < 0) or (y >= len(s)):
                break
            elif s[y][x] == 'L':
                break
            elif s[y][x] == '#':
                unwanted = True
            if adjacent:
                break
        counter += int(unwanted)
    return counter


def run_it(seats, rule_params):
    changes = -1
    while changes != 0:
        print('.', end='')
        s_new = [i for i in seats]
        changes = 0
        for y in range(0, len(seats)):
            for x in range(0, len(seats[y])):
                if (free_direction_count(seats, x, y, rule_params[0]) >= rule_params[1]) and (seats[y][x] == '#'):
                    s_new[y] = s_new[y][:x] + 'L' + s_new[y][x+1:]
                    changes += 1
                if (free_direction_count(seats, x, y, rule_params[0]) == 0) and (seats[y][x] == 'L'):
                    s_new[y] = s_new[y][:x] + '#' + s_new[y][x + 1:]
                    changes += 1
        seats = s_new
    occupied = 0
    for row in seats:
        occupied += row.count('#')
    return occupied


if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_11.txt').read_text().split('\n')]
    print('Answer part 1 = {:d} '.format(run_it(dataset, [True, 4])))
    print('Answer part 2 = {:d} '.format(run_it(dataset, [False, 5])))



