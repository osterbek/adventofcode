from pathlib import Path


def recursive_combat(deck_player_1, deck_player_2):
    already_seen_this_way = {}
    while len(deck_player_1) * len(deck_player_2) != 0:
        if str((deck_player_1, deck_player_2)) in already_seen_this_way.keys():
            return [1, []]
        else:
            already_seen_this_way[str((deck_player_1, deck_player_2))] = True
            top_card_player_1 = deck_player_1.pop(0)
            top_card_player_2 = deck_player_2.pop(0)
            if len(deck_player_1) < top_card_player_1 or len(deck_player_2) < top_card_player_2:
                if top_card_player_1 > top_card_player_2:
                    deck_player_1.extend([top_card_player_1, top_card_player_2])
                else:
                    deck_player_2.extend([top_card_player_2, top_card_player_1])
            else:
                if recursive_combat(deck_player_1.copy()[:top_card_player_1], deck_player_2.copy()[:top_card_player_2])[0] == 1:
                    deck_player_1.extend([top_card_player_1, top_card_player_2])
                else:
                    deck_player_2.extend([top_card_player_2, top_card_player_1])
    if len(deck_player_2) == 0:
        return [1, deck_player_1]
    else:
        return [2, deck_player_2]


if __name__ == '__main__':
    dataset = [i for i in Path('../input/input_2020_22.txt').read_text().split('\n\n')]
    deck_player_1 = [int(i) for i in dataset[0].split('\n')[1:]]
    deck_player_2 = [int(i) for i in dataset[1].split('\n')[1:]]
    winner_deck = []
    answer_1, answer_2 = 0, 0
    while len(deck_player_1) * len(deck_player_2) != 0:
        top_card_player_1 = deck_player_1.pop(0)
        top_card_player_2 = deck_player_2.pop(0)
        if top_card_player_1 >= top_card_player_2:
            deck_player_1.extend([top_card_player_1, top_card_player_2])
            winner_deck = deck_player_1
        else:
            deck_player_2.extend([top_card_player_2, top_card_player_1])
            winner_deck = deck_player_2
    for i in range(0, len(winner_deck)):
        answer_1 += (len(winner_deck) - i) * winner_deck[i]
    print('Answer part 1 = {:d} '.format(answer_1), answer_1 == 31629)
    deck_player_1 = [int(i) for i in dataset[0].split('\n')[1:]]
    deck_player_2 = [int(i) for i in dataset[1].split('\n')[1:]]
    [winner, winner_deck] = recursive_combat(deck_player_1, deck_player_2)
    for i in range(0, len(winner_deck)):
        answer_2 += (len(winner_deck) - i) * winner_deck[i]
    print('Answer part 2 = {:d} '.format(answer_2), answer_2 == 35196)
