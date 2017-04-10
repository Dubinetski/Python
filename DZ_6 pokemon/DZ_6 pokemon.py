# Написать игру в слова на тему "покемоны"
# взять их список тут https://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon
# 1 компьютер играет с человеком (неважно кто начинает (как реализуете))
# 2 комп контролирует соблюдение правил

import re


# выделяет из файла список покемонов
def pokemon_parser(file_name):
    with open(file_name, 'r') as f:
        # (?:\n?\t?No \D+)? для фильтрации фразы 'No additional Pokémon'
        # (?:\s?\d+\s) для фильтрации номеров покемонов с пробельными символами
        list = re.split('(?:\n?\t?No \D+)?(?:\s?\d+\s)', f.read())[1:]
    return list


# составляет из списка покемонов словарь группируя по первой букве
def dict_from_pokemon_list(list):
    dict = {chr(a): [] for a in range(65, 91)}  # генератор словаря - (буква A-Z): список
    for pok in list:
        dict[pok[:1]].append(pok)
    return dict


# определение колличества возможных вариантов ответа
def count_of_choices(dict, name):
    return len(dict[name[-1].upper()])


# ход игрока
def user_motion(pok_dict, last_letter):
    while True:
        pok = input('You: ')
        if (last_letter.upper() != pok[:1]) and (last_letter != ' '):
            print('Incorrect name. First letter of name mast be ' + last_letter.upper())
            continue
        elif pok not in pok_dict[pok[:1]]:
            print('Such pokemon is not exist. Choice another name of pokemon.')
            continue
        break
        pok_dict[pok[:1]].remove(pok)
    if count_of_choices(pok_dict, pok) == 0:
        input('\nYou win.')
        exit(0)
    return pok


# ход компьютера
def comp_motion(pok_dict, last_letter):
    possible_choice = pok_dict[last_letter.upper()]
    pok = possible_choice[0]
    min_rating = 100
    for possible_pokemon in possible_choice:
        rating = count_of_choices(pok_dict, possible_pokemon)
        if rating <= min_rating:
            pok = possible_pokemon
            min_rating = rating
    print('Comp: ' + pok)
    pok_dict[pok[:1]].remove(pok)
    if min_rating == 0:
        input('\nIsn\'t pokemon on ' + pok[-1].upper() + 'Comp is win')
        exit(0)
    return pok


if __name__ == '__main__':
    print('Game to WORD. Them - POKEMON\n')

    pokemon_list = pokemon_parser('Pokemon.txt')
    pokemon_dict = dict_from_pokemon_list(pokemon_list)

    print('You start. Say the name of the first pokemon.')
    pokemon = ' '

    while True:
        pokemon = user_motion(pokemon_dict, pokemon[-1])
        pokemon = comp_motion(pokemon_dict, pokemon[-1])
