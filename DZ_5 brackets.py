# Проверить корректность расстановки скобок в строке
# проверять 3 вида скобок: []{}()
# !!!! оценивается красота кода


def check_brackets(line):
    brackets = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
    no_close = {}
    for symbol in line:
        if symbol in brackets:
            brackets[symbol] += 1
            no_close = {'()': brackets['('] - brackets[')'],
                        '[]': brackets['['] - brackets[']'],
                        '{}': brackets['{'] - brackets['}']}
            for key in no_close:
                if no_close[key] < 0:
                    return 'mistaken'
            if (symbol == ('{' or '}') and (no_close['()'] or no_close['[]'])) or \
                    (symbol == ('[' or ']') and no_close['()']):
                return 'mistaken'
    if not sum(brackets.values()):
        return 'absence'
    if sum(no_close.values()):
        return 'mistaken'
    return 'correct'


if __name__ == '__main__':
    print('Program check correct of placing brackets () [] and {} in expression.\n')
    expression = input('Write the expression: ')

    while True:
        print('Brackets is ' + check_brackets(expression) + '.')
        expression = input('Write another expression for checking (empty string -> EXIT)\n\n')
        if expression == (''):
            break
