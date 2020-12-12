from pathlib import Path


def part_1(ds):
    pathways = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    directions = ['E', 'S', 'W', 'N']
    x = 0
    y = 0
    face = 0
    for move in ds:
        cmd = move[0]
        value = int(move[1:])
        if cmd == 'F':
            x += pathways[face][0] * value
            y += pathways[face][1] * value
        elif cmd in directions:
            x += pathways[directions.index(cmd)][0] * value
            y += pathways[directions.index(cmd)][1] * value
        elif cmd == 'L':
            face += (3 * value//90)
        elif cmd == 'R':
            face += value//90
        while face > 3:
            face -= 4
    return abs(x) + abs(y)


def part_2(ds, wpx, wpy):
    pathways = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    directions = ['E', 'S', 'W', 'N']
    x = 0
    y = 0
    for move in ds:
        cmd = move[0]
        value = int(move[1:])
        if cmd == 'F':
            x += wpx * value
            y += wpy * value
        elif cmd in directions:
            wpx += pathways[directions.index(cmd)][0] * value
            wpy += pathways[directions.index(cmd)][1] * value
        elif cmd in ['L', 'R']:
            if value == 180:
                wpx = - wpx
                wpy = - wpy
            elif ((cmd == 'L') and (value == 90)) or ((cmd == 'R') and (value == 270)):
                tmp = wpx
                wpx = - wpy
                wpy = tmp
            elif ((cmd == 'L') and (value == 270)) or ((cmd == 'R') and (value == 90)):
                tmp = wpx
                wpx = wpy
                wpy = - tmp
    return abs(x) + abs(y)


if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_12.txt').read_text().split('\n')]
    print('Answer part 1 = {:d} '.format(part_1(dataset)))
    print('Answer part 2 = {:d} '.format(part_2(dataset, 10, 1)))



