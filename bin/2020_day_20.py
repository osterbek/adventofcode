from pathlib import Path


if __name__ == '__main__':
    ds = [i for i in Path('../input/input_2020_20.txt').read_text().split('\n\n')]
    tiles = []
    for t in range(0, len(ds)):
        border = ['' for i in range(0, 4)]
        for i in range(0, 10):
            border[0] += ds[t][i + 11]
            border[1] += ds[t][(i + 1) * 11 + 9]
            border[2] += ds[t][110 + i]
            border[3] += ds[t][(i + 1) * 11]
        tiles.append([int(ds[t][5:9]), border])
    answer_1 = 1
    for tile_1 in range(0, len(ds)):
        adjacent = 0
        for rotation_1 in range(0, 4):
            for tile_2 in range(0, len(ds)):
                for rotation_2 in range(0, 4):
                    if tile_1 != tile_2:
                        for inversion in (-1, 1):
                            if tiles[tile_1][1][rotation_1] == tiles[tile_2][1][rotation_2][::inversion]:
                                adjacent += 1
        if adjacent == 2:
            answer_1 *= tiles[tile_1][0]
    print('Answer part 1 = {:d} '.format(answer_1), answer_1 == 12519494280967)
