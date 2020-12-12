from pathlib import Path
import re


def field_check(text, field_type):
    match = ['[0-9]{4}', '[0-9]{4}', '[0-9]{4}', '', '#[0-9a-f]{6}', '','[0-9]{9}', '']
    border = [[1902, 2002], [2010, 2020], [2020, 2030], [-1, -1], [-1, -1], [-1, -1], [0, 999999999], [-1, -1]]
    okay = True
    if field_type in [0, 1, 2, 6]:
        if re.fullmatch(match[field_type], text):
            okay = (int(text) >= border[field_type][0]) and (int(text) <= border[field_type][1])
        else:
            okay = False
    elif field_type == 3:
        if re.match('[0-9]', text[:-2]):
            okay = ((int(text[:-2]) >= 150) and (int(text[:-2]) <= 193) and (text[-2:] == 'cm')) \
                   or ((int(text[:-2]) >= 59) and (int(text[:-2]) <= 76) and (text[-2:] == 'in'))
        else:
            okay = False
    elif field_type == 4:
        okay = bool(re.fullmatch(match[field_type], text))
    elif field_type == 5:
        okay = text in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif field_type == 7:
        okay = True
    return okay


if __name__ == '__main__':
    datset = [i for i in Path('../input/input_2020_04.txt').read_text().split('\n\n')]
    key = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    answer_1 = 0
    answer_2 = 0
    for passport in datset:
        fields = [i for i in passport.replace('\n', ' ').split(' ')]
        check_1 = [0 for i in (range(0, len(key)))]
        check_2 = [0 for i in (range(0, len(key)))]
        for f in fields:
            field_type = key.index(f[0:3])
            check_1[field_type] = 1
            check_2[field_type] = int(field_check(f[4:], field_type))
        answer_1 += (sum(check_1[0:7]) == 7)
        answer_2 += (sum(check_2[0:7]) == 7)
    print('Answer part 1 = {:d} '.format(answer_1))
    print('Answer part 2 = {:d} '.format(answer_2))


