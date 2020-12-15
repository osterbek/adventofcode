from pathlib import Path


if __name__ == '__main__':
    spoken = [int(i) for i in Path('../input/input_2020_15.txt').read_text().split(',')]
    history = {}
    for i in range(0, len(spoken) - 1):
        history[spoken[i]] = i
    while len(spoken) < 30000000:
        number = max(0, len(spoken) - 1 - history.get(spoken[-1], len(spoken) + 999))
        history[spoken[-1]] = len(spoken) - 1
        spoken.append(number)
        if len(spoken) == 2020:
            print('Answer part 1 = {:d} '.format(spoken[-1]), (spoken[-1] == 249))
    print('Answer part 1 = {:d} '.format(spoken[-1]), (spoken[-1] == 41687))
