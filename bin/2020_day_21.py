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
    possib_ing_per_aller = [[] for i in allergens]
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
                possib_ing_per_aller[allergen].append(i)
    print(possib_ing_per_aller)
    something_changed = True
    while something_changed:
        something_changed = False
        for allergen in range(0, len(allergens)):
            if len(possib_ing_per_aller[allergen]) == 1:
                for allergen_2 in range(0, len(allergens)):
                    if allergen_2 != allergen and possib_ing_per_aller[allergen][0] in possib_ing_per_aller[allergen_2]:
                        possib_ing_per_aller[allergen_2].remove(possib_ing_per_aller[allergen][0])
                        something_changed = True
    canon_dang_ingr = [[possib_ing_per_aller[i][0], allergens[i]] for i in range(0, len(allergens))]
    for i in range(0, len(allergens) - 1):
        for j in range(0, len(allergens) - 1):
            if canon_dang_ingr[j][1] > canon_dang_ingr[j+1][1]:
                temp = canon_dang_ingr[j]
                canon_dang_ingr[j] = canon_dang_ingr[j+1]
                canon_dang_ingr[j+1] = temp
    answer_1 = sum([sum([int(not (i in [p[0] for p in possib_ing_per_aller])) for i in f[0]]) for f in food])
    answer_2 = str([i[0] for i in canon_dang_ingr]).replace(' ', '').replace('[', '').replace(']', '').replace('\'', '')
    print('Answer part 1 = {:d} '.format(answer_1), answer_1 == 2211)
    print('Answer part 2 = ' + answer_2 + ' ' + str(answer_2 == 'vv,nlxsmb,rnbhjk,bvnkk,ttxvphb,qmkz,trmzkcfg,jpvz'))
