from pathlib import Path


def year2020_day03_core(ds, right, down):
    answer = 0
    x = 0
    y = down
    amplitude = len(ds[0])
    while y < len(ds):
        x += right
        if x >= amplitude:
            x = x - amplitude
        if ds[y][x] == '#':
            answer += 1
        y += down
    return answer


if __name__ == '__main__':
    ds = Path('../input/input_2020_03.txt').read_text().split('\n')

    variants = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    answer2 = 1
    for i in range(0, len(variants)):
        answer2 = answer2 * year2020_day03_core(ds, variants[i][0], variants[i][1])

    print('Answer part 1 = {:d} '.format(year2020_day03_core(ds, 3, 1)))
    print('Answer part 2 = {:d} '.format(answer2))
