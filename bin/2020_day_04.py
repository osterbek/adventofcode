from pathlib import Path
import re


def field_check(text, field_type):
    okay = True
    if field_type == 0:
        try:
            if (int(text) >= 1920) and (int(text) <= 2002):
                okay = True
            else:
                okay = False
        except ValueError:
            okay = False
    elif field_type == 1:
        try:
            if (int(text) >= 2010) and (int(text) <= 2020):
                okay = True
            else:
                okay = False
        except ValueError:
            okay = False
    elif field_type == 2:
        try:
            if (int(text) >= 2020) and (int(text) <= 2030):
                okay = True
            else:
                okay = False
        except ValueError:
            okay = False
    elif field_type == 3:
        temp = text[-2:]
        if temp in ['cm', 'in']:
            try:
                value = int(text[:-2])
                if temp == 'cm':
                    if (value <= 193) and (value >= 150):
                        okay = True
                    else:
                        okay = False
                else:
                    if (value <= 76) and (value >= 59):
                        okay = True
                    else:
                        okay = False
            except ValueError:
                okay = False
        else:
            okay = False
    elif field_type == 4:
        if (text[0] == '#') and (len(text) == 7):
            okay = True
            for i in range(1, 7):
                if text[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                    okay = True
                else:
                    okay = False
        else:
            okay = False
    elif field_type == 5:
        if text in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            okay = True
        else:
            okay = False
    elif field_type == 6:
        if len(text) == 9:
            try:
                temp = int(text)
                okay = True
            except ValueError:
                okay = False
        else:
            okay = False
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
            if field_check(f[4:], field_type):
                check_2[field_type] = 1
        answer_1 += (sum(check_1[0:7]) == 7)
        answer_2 += (sum(check_2[0:7]) == 7)
    print('Answer part 1 = {:d} '.format(answer_1))
    print('Answer part 2 = {:d} '.format(answer_2))
    
