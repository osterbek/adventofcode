from pathlib import Path

if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_21.txt').read_text().split('\n')]
    food, ingredients, allergens = [], [], []
    for item in dataset:
        ingre = item.split('(')[0][:-1].split(' ')
        aller = item.split('(')[1][9:-1].split(', ')
        food.append([ingre, aller])
        ingredients.extend(ingre)
        allergens.extend(aller)
    ingredients = list(set(ingredients))
    allergens = list(set(allergens))
    possible = [[] for i in allergens]
    for allergen in range(0, len(allergens)):
        ingredient_candidates = []
        for f in food:
            if allergens[allergen] in f[1]:
                ingredient_candidates.append(f[0])
        for i in ingredient_candidates[0]:
            intersection = True
            for j in ingredient_candidates[1:]:
                if not (i in j):
                    intersection = False
            if intersection:
                possible[allergen].append(i)
    something_changed = True
    while something_changed:
        something_changed = False
        for allergen in range(0, len(allergens)):
            if len(possible[allergen]) == 1:
                for allergen_2 in range(0, len(allergens)):
                    if allergen_2 != allergen:
                        if possible[allergen][0] in possible[allergen_2]:
                            possible[allergen_2].remove(possible[allergen][0])
                            something_changed = True
    answer_1 = 0
    for f in food:
        for i in f[0]:
            if not (i in [p[0] for p in possible]):
                answer_1 += 1
    print('Answer part 1 = {:d} '.format(answer_1), answer_1 == 2211)
    canon_dang_ingr = []
    for i in range(0, len(allergens)):
        canon_dang_ingr.append([possible[i][0], allergens[i]])
    for i in range(0, len(allergens) - 1):
        for j in range(0, len(allergens) - 1):
            if canon_dang_ingr[j][1] > canon_dang_ingr[j+1][1]:
                temp = canon_dang_ingr[j]
                canon_dang_ingr[j] = canon_dang_ingr[j+1]
                canon_dang_ingr[j+1] = temp
    answer_2 = str([i[0] for i in canon_dang_ingr]).replace(' ', '').replace('[', '').replace(']', '').replace('\'', '')
    print('Answer part 2 = ' + answer_2 + ' ' + str(answer_2 == 'vv,nlxsmb,rnbhjk,bvnkk,ttxvphb,qmkz,trmzkcfg,jpvz'))
    
