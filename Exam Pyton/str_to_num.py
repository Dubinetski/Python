dict_multiply = {'тыс': 10 ** 3, 'миллион': 10 ** 6, 'миллиар': 10 ** 9, 'три': 10 ** 12,
                 'ква': 10 ** 15, 'кви': 10 ** 18, 'сек': 10 ** 21, 'сеп': 10 ** 24,
                 'окт': 10 ** 27, 'нон': 10 ** 30, 'дец': 10 ** 33}

dict_summ = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8,
             'девять': 9, 'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14,
             'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
             'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,
             'восемьдесят': 80, 'девяносто': 90, 'сто': 100, 'двести': 200, 'триста': 300, 'четыреста': 400,
             'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700, 'восемьсот': 800, 'девятьсот': 900, 'одна': 1, 'две': 2}


def str_to_int(str_number):
    number = 0
    rezult_number = 0
    str_number_list = str_number.split()
    for elem in str_number_list:
        if elem in dict_summ:
            number += dict_summ[elem]
        elif elem[:3] in dict_multiply:
            number *= dict_multiply[elem[:3]]
            rezult_number += number
            number = 0
        elif elem[:7] in dict_multiply:  # для миллионов и миллиардов
            number *= dict_multiply[elem[:7]]
            rezult_number += number
            number = 0
    rezult_number += number

    return rezult_number


def common_denominator(denominator_in_string):
    if denominator_in_string.find('десят') > -1:
        denominator = 10
    elif denominator_in_string.find('сот') > -1 or denominator_in_string.find('сто') > -1:
        denominator = 100
    else:
        denominator = 1

    for key in dict_multiply:
        if denominator_in_string.find(key) > -1:
            denominator *= dict_multiply[key]
            break

    return denominator


def convert_to_number(str_number):
    number_list = [str_number]
    if str_number.find('целых') > -1:
        number_list = str_number.split('целых')
    elif str_number.find('целая') > -1:
        number_list = str_number.split('целая')

    fractional_part = 0

    integer_part = str_to_int(number_list[0])
    if len(number_list) > 1:
        fractional_part_list = number_list[1].split()
        fractional_part = str_to_int(' '.join(fractional_part_list[:-1]))
        denominator = common_denominator(fractional_part_list[-1])
        fractional_part /= denominator

    return integer_part + fractional_part


if __name__ == '__main__':
    while True:
        number = input("Write the number in words: ")
        string = convert_to_number(number)
        if string == 0 and not number == '':
            print('Incorrect number. Please try again.\n')
        break

    print('Число: ' + str(convert_to_number(number)))
    input()
