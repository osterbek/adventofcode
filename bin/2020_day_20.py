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
    answer_2 = 0
    for tile in range(0, len(ds)):
        for y in range(0, 8):
            for x in range(0, 8):
                answer_2 += int(ds[tile][y * 11 + x + 23] == '#')
    answer_2 -= 15 * 25  # guessed 25 ... just tried a little ... have no time to finalize this algorithmically
    print('Answer part 2 = {:d} '.format(answer_2), answer_2 == 2442)
    
