import re
result = 0
warning = 'Incorrect entering. Please try again'

print('Calculator (use + - * / ^).\n(Double-clicking ENTER -> exit)\n')

while True:
    expressing = input()
    if expressing == '':
        break

    list_of_numbers = re.findall('(?<=[-+*/^])(?:-\d+\.?\d*)+|(?:\d+\.?\d*)+', expressing)  # список операндов
    list_of_operators = re.findall('([-+*/^])(?:[-\d])', expressing)  # список операторов

    # проверка корректности ввода
    if len(expressing) != len(''.join(list_of_numbers)) + len(''.join(list_of_operators))\
            or (len(''.join(re.split('[-+*/^\d.]+', expressing))) > 0):
        print(warning)
        continue

    def plus(a, b): return a+b
    def minus(a, b): return a-b
    def multiplication(a, b): return a*b
    def division(a, b): return a/b
    def degree(a, b): return a**b
    def not_imp(a, b): print(warning)

    # использование словаря в качестве оператора switch()
    dict_as_switch = {
        "+": plus,
        "-": minus,
        "*": multiplication,
        "/": division,
        "^": degree}

    first_symbol = expressing[0]
    if (first_symbol == "-")or(first_symbol == "+")or(first_symbol == "*")or(first_symbol == "/")or(first_symbol == "^"):
        list_of_numbers.insert(0, result)
    else: result = float(list_of_numbers[0])

    for i in range(len(list_of_numbers)-1):
        if list_of_operators[i] == '/' and list_of_numbers[i+1] == '0':
            print('Division by zero')
            continue
        result = dict_as_switch.get(list_of_operators[i], not_imp)(result, float(list_of_numbers[i+1]))

    print(result)