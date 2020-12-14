d = int(input('Введите cрок размещения капитала '))  # Срок размещения капитала в годах
s = int(input("Введите начальный капитал "))  # Начальный капитал
pc = int(input('Введите процентную ставку в процентах '))  # процентная ставка
invest = int(input("Введите размер инвестиционных вливаний "))  # размер инвестиционных вливаний

for i in range(1, d + 1):
    print(i, 'год')
    print('-' * 53)
    print('|         |    основа    |  сумма %   |              |\n|  месяц  |  инвестиций  |  за месяц  |   капитал    |')
    print('-' * 53)
    for i in range(1, 13):
        if len(str(i)) < 2:
            print('|   ', i, '   |', end='')
        else:
            print('|  ', i, '   |', end='')
        if len(format(s, '.2f')) < 14:
            j = 14 - len(format(s, '.2f'))
            print(format(s, '.2f'), +j * " ", '|', sep='', end='')
        else:
            print(format(s, '.2f'), '|', end='')
        if len(format((1+pc/100) * s - s, '.2f')) < 12:
            h = 12 - len(format((1+pc/100) * s - s, '.2f'))
            print(format((1+pc/100) * s - s, '.2f'), +h * " ", '|', sep='', end='')
        else:
            print(format((1+pc/100) * s - s, '.2f'), '|', sep='', end='')
        s *= (1+pc/100)
        if len(format(s, '.2f')) < 14:
            k = 14 - len(format(s, '.2f'))
            print(format(s, '.2f'), +k * " ", '|', sep="", end='\n')
        else:
            print(format(s, '.2f'), '|', sep="", end='\n')
        s += invest
    print('-' * 47)
