
d = int(input('Введите cрок размещения капитала '))  # Срок размещения капитала в годах
s = int(input("Введите начальный капитал "))  # Начальный капитал
pc = float(input('Введите процентную ставку в процентах '))  # процентная ставка
invest = int(input("Введите размер инвестиционных вливаний "))  # размер инвестиционных вливаний

for i in range(1, d + 1):
    print(i, 'год\n', '-' * 54, '\n|         |    основа    |  сумма %   |              |\n|  месяц  |  инвестиций  |  за месяц  |   капитал    |\n', '-' * 54)
    for i in range(1, 13):
        print('|  ' + ' ' * (2 - len(str(i))), i, '   |', format(s, '.2f') + (14 - len(format(s, '.2f'))) * " ", '|', format((1+pc/100) * s - s, '.2f') + (12 - len(format((1+pc/100) * s - s, '.2f'))) * " ", '|', sep='', end='')
        s *= (1+pc/100)
        print(format(s, '.2f') + (14 - len(format(s, '.2f'))) * " ", '|', sep='')
        s += invest
    print('-' * 54)
    