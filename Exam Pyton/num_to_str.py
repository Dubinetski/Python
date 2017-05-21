# Все варианты написания разрядов
digit_place_str = ['', 'тысяч', 'миллион', 'миллиард', 'триллион', 'квадриллион', 'квинтиллион', 'секстиллион',
                   'септиллион', 'октиллион', 'нониллион', 'дециллион']

#  Все варианты написания чисел от 0 до 999
number_str_list = ['ноль',
                   ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять'],
                   ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
                    'семнадцать', 'восемнадцать', 'девятнадцать'],
                   ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
                    'девяносто'],
                   ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот',
                    'девятьсот'],
                   ['', 'одна', 'две']]


# Добавление разряда, с учетом окончания
def number_rank_name(three_digit, three_digit_place):
    if three_digit_place == 0:  # кроме "первой тройки"
        return ''
    num_str_ending = [['а', 'и', ''],  # для тысяч
                      ['', 'а', 'ов']]
    num_ending_version = 0 if three_digit_place == 1 else 1

    last_cipher = three_digit[-1]
    second_cipher = three_digit[-2:-1]
    rezult_str = ' ' + digit_place_str[three_digit_place]

    if last_cipher == '1' and not second_cipher == '1':  # если оканчивается на 1, но не 11
        rezult_str += num_str_ending[num_ending_version][0]
    elif last_cipher in ('2', '3', '4') and not second_cipher == '1':  # если оканчивается на 2, 3 или 4
        rezult_str += num_str_ending[num_ending_version][1]
    else:
        rezult_str += num_str_ending[num_ending_version][2]
    return rezult_str

# Соединяеть список строк троек цифр числа в одну строку
def join_in_str(str_list):
    rezult_str = ''
    for string in str_list:
        if string:  # если тройка цифр не пустая
            if rezult_str:  # если результирующая строка не пустая, т.е. тройка цифр не первая
                rezult_str += ' '
            rezult_str += string
    return rezult_str


# Преобразование трехзначного числа в строку
def three_digit_number_in_string(three_digit, three_digit_place):
    if int(three_digit) == 0:  # пропускаем нулевые тройки чисел
        return ''
    rezult_str = ''
    cipher_place = 0
    for cipher in three_digit:
        if rezult_str and cipher_place and int(cipher):
            rezult_str += ' '
        if not int(cipher):
            pass
        elif cipher_place == 0:  # сотни
            rezult_str += number_str_list[4][int(cipher)]
        elif cipher_place == 1:  # десятки
            if int(cipher) == 1:  # от 10 до 19
                rezult_str += number_str_list[2][int(three_digit[-1])]
                break
            else:
                rezult_str += number_str_list[3][int(cipher)]
        elif cipher_place == 2:  # единицы
            if (three_digit_place == 1) and (int(cipher) <= 2):  # если 1 или 2 и находится в тройке тысяч
                rezult_str += number_str_list[5][int(cipher)]
            else:
                rezult_str += number_str_list[1][int(cipher)]
        cipher_place += 1

    rezult_str += number_rank_name(three_digit, three_digit_place)

    return rezult_str


# Перевод числа в строчную запись
def number_to_string(int_number):
    try:
        int(int_number)
    except ValueError:
        return 'Number is not integer\n'

    number = str(int_number)

    if number == '0':
        return number_str_list[0]  # Если число ноль, сразу сообщить об этом и выйти

    # дополним длину числа до кратной 3 ведущими нулями (без подключения модуля math)
    num_str = number.zfill((len(number) // 3 + (len(number) % 3 > 0)) * 3)
    # разделим строку на тройки цифр в обратном порядке
    three_digit_group = [num_str[k - 3:k] for k in range(len(num_str), 2, -3)]

    rezult_str_list = []

    # обработаем каждую тройку чисел отдельно
    three_digit_place = 0
    for three_digit in three_digit_group:
        rezult_str_list.append(three_digit_number_in_string(three_digit, three_digit_place))
        three_digit_place += 1

    rezult_str_list.reverse()  # возвращаем изначальный порядок троек цифр числа

    return join_in_str(rezult_str_list)


# Формирует название целой части вещественного числа
def str_integer_part(number):
    number = str(number)
    str_number = number_to_string(number)

    if number[-2:-1] == '1' or int(number[-1]) > 3 or number[-1] == '0':
        return str_number + ' целых'
    else:
        if number[-1] == '1':
            return str_number[:-2] + 'на целая'
        elif number[-1] in ('2', '3'):
            return str_number[:-1] + 'е целые'


# Формирует название дробной части вещественного числа
def str_fractional_part(fractional_part):
    for i in range(len(fractional_part), 0, -1):  # отбрасываем лишние нули "справа"
        if int(fractional_part[i - 1]):
            fractional_part = fractional_part[:i]
            break

    str_number = number_to_string(fractional_part)

    str_category = [['', 'десят', 'сот'],  # для десятых и сотых
                    ['', 'десяти', 'сто']]  # для всех остальных

    length_number = len(fractional_part)
    # название степени дробной части
    ending = str_category[length_number // 3 > 0][length_number % 3] + digit_place_str[length_number // 3]

    # "склеивание" названия дробной части числа
    if fractional_part[-2:-1] == '1' or int(fractional_part[-1]) > 2:  # оканчивается на 3-9 либо на 10-12
        str_number += ' ' + ending + 'ных'
    else:
        if fractional_part[-1] == '1':  # оканчивается на 1
            str_number = str_number[:-2] + 'на ' + ending + 'ная'
        elif fractional_part[-1] == '2':  # оканчивается на 2
            str_number = str_number[:-1] + 'е ' + ending + 'ные'

    return str_number


def convert_to_string(number):
    number = number.split('.')
    if len(number) == 2:  # если имеется дробная часть
        return str_integer_part(number[0]) + ' ' + str_fractional_part(number[1])
    else:
        return number_to_string(number[0])


if __name__ == '__main__':
    while True:
        number = input("Write the number: ")
        try:
            float(number)
            break
        except ValueError:
            print('Incorrect number. Please try again.\n')

    print('Число прописью: ' + convert_to_string(number))
