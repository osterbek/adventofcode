from pathlib import Path


def field_check(text, type):
    okay = True
    if type == 0:
        try:
            if (int(text) >= 1920) and (int(text) <= 2002):
                okay = True
            else:
                okay = False
        except ValueError:
            okay = False
    elif type == 1:
        try:
            if (int(text) >= 2010) and (int(text) <= 2020):
                okay = True
            else:
                okay = False
        except ValueError:
            okay = False
    elif type == 2:
        try:
            if (int(text) >= 2020) and (int(text) <= 2030):
                okay = True
            else:
                okay = False
        except ValueError:
            okay = False
    elif type == 3:
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
    elif type == 4:
        if (text[0] == '#') and (len(text) == 7):
            okay = True
            for i in range(1, 7):
                if text[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                    okay = True
                else:
                    okay = False
        else:
            okay = False
    elif type == 5:
        if text in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            okay = True
        else:
            okay = False
    elif type == 6:
        if len(text) == 9:
            try:
                temp = int(text)
                okay = True
            except ValueError:
                okay = False
        else:
            okay = False
    elif type == 7:
        okay = True
    return okay


if __name__ == '__main__':
    f = open('../input/input_2020_04.txt')
    ds = []
    for line in f.readlines():
        ds.append(line)
    f.close()
    key = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    passport = 0
    pass_fields = [[False for i in (range(0, 8))]]
    for i in range(0, len(ds)):
        if len(ds[i]) == 1:
            passport += 1
            pass_fields.append([False for i in (range(0, 8))])
        else:
            for j in range(0, len(key)):
                if ds[i].find(key[j]+':') >= 0:
                    temp = ds[i][ds[i].find(key[j]+':')+4:]
                    pass_fields[passport][j] = temp[:temp.find(' ')]
    answer1 = 0
    answer2 = 0
    for i in range(0, passport+1):
        okay1 = 1
        okay2 = 1
        for j in range(0, 7):
            if not pass_fields[i][j]:
                okay1 = 0
                okay2 = 0
            else:
                if not field_check(pass_fields[i][j], j):
                    okay2 = 0
        answer1 += okay1
        answer2 += okay2
    print('Answer part 1 = {:d} '.format(answer1))
    print('Answer part 2 = {:d} '.format(answer2))
