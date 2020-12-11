from pathlib import Path

if __name__ == '__main__':
    dataset = [int(i) for i in Path('../input/input_2020_09.txt').read_text().split('\n')]
    preamble = 25

    pointer = preamble
    answer_1 = 0
    while answer_1 == 0:
        found = False
        for i in range(1, preamble + 1):
            for j in range(1, preamble + 1):
                if (i != j) and (dataset[pointer - i] + dataset[pointer - j] == dataset[pointer]):
                    found = True
        if not found:
            answer_1 = dataset[pointer]
        else:
            pointer += 1

    answer_2 = 0
    for i in range(0, pointer):
        s = 0
        for j in range(i, pointer):
            s += dataset[j]
            if s == answer_1:
                slice_2 = dataset[i:j+1]
                answer_2 = min(slice_2) + max(slice_2)

    print('Answer part 1 = {:d} '.format(answer_1))
    print('Answer part 2 = {:d} '.format(answer_2))

    

