from pathlib import Path


def neighbours(a):
    answer = []
    for direction in range(0, len(orientation[1])):
        answer.append((a[0] + orientation[1][direction][0], a[1] + orientation[1][direction][1]))
    return answer


if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_24.txt').read_text().split('\n')]
    orientation = [['e', 'se', 'sw', 'w', 'nw', 'ne'], [[2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1], [1, -1]]]
    floor = {}
    for tile in range(0, len(dataset)):
        position = [0, 0]
        char = 0
        while char < len(dataset[tile]):
            if dataset[tile][char] not in ['e', 'w']:
                way = dataset[tile][char] + dataset[tile][char + 1]
                char += 2
            else:
                way = dataset[tile][char]
                char += 1
            position[0] += orientation[1][orientation[0].index(way)][0]
            position[1] += orientation[1][orientation[0].index(way)][1]
        if (position[0], position[1]) in floor.keys():
            del floor[(position[0], position[1])]
        else:
            floor[(position[0], position[1])] = 1
    answer_1 = sum([floor[i] for i in floor.keys()])
    print('Answer part 1 = {:d} '.format(answer_1), answer_1 == 512)
    for day in range(0, 100):
        shadow = floor.copy()
        for tile_1 in floor.keys():
            neighbours_counter = 0
            for tile_2 in floor.keys():
                if tile_2 in neighbours(tile_1):
                    neighbours_counter += 1
            if neighbours_counter > 2 or neighbours_counter == 0:
                del shadow[tile_1]
            for tile_2 in neighbours(tile_1):
                if tile_2 not in floor.keys():
                    neighbours_counter = 0
                    for tile_3 in neighbours(tile_2):
                        if tile_3 in floor.keys():
                            neighbours_counter += 1
                    if neighbours_counter == 2:
                        shadow[tile_2] = 1
        floor = shadow.copy()
        print(day, sum([floor[i] for i in floor.keys()]))
    print('Answer part 2 = {:d} '.format(sum([floor[i] for i in floor.keys()])), sum([floor[i] for i in floor.keys()]) == 4120)
