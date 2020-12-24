from pathlib import Path


if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_24.txt').read_text().split('\n')]
    flipped = {}
    directions = [['e', 'se', 'sw', 'w', 'nw', 'ne'], [[2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1], [1, -1]]]
    for tile in range(0, len(dataset)):
        coordinate = [0, 0]
        char = 0
        while char < len(dataset[tile]):
            if dataset[tile][char] not in ['e', 'w']:
                direction = dataset[tile][char] + dataset[tile][char + 1]
                char += 2
            else:
                direction = dataset[tile][char]
                char += 1
            coordinate[0] += directions[1][directions[0].index(direction)][0]
            coordinate[1] += directions[1][directions[0].index(direction)][1]
        if str(coordinate) in flipped.keys():
            flipped[str(coordinate)] = 0
        else:
            flipped[str(coordinate)] = 1
    answer_1 = sum([flipped[i] for i in flipped.keys()])
    print('Answer part 1 = {:d} '.format(answer_1), answer_1 == 512)
