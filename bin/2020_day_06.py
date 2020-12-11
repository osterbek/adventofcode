from pathlib import Path


if __name__ == '__main__':
    content = Path('../input/input_2020_06.txt').read_text().split('\n\n')
    dataset = []
    for group in range(0, len(content)):
        dataset.append(content[group].split('\n'))
    questions = [chr(value) for value in range(97, 123)]
    solution = [0, 0]
    for group in range(0, len(dataset)):
        yes = [0 for letter in range(0, len(questions))]
        for person in range(0, len(dataset[group])):
            for letter in range(0, len(questions)):
                if questions[letter] in dataset[group][person]:
                    yes[letter] += 1
        for letter in range(0, len(questions)):
            solution[0] += (yes[letter] > 0)
            solution[1] += (yes[letter] == len(dataset[group]))
    print('Answer part 1 = {:d} '.format(solution[0]))
    print('Answer part 2 = {:d} '.format(solution[1]))
