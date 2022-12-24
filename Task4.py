# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

num = int(input('Введите количество журавликов: '))

boy = num // 6 # делим на 6, т.к. по логике решения надо разделить общее количество журавликов на 2(Катя в 2 раза больше), 
               # а потом на 3(количество детей)
girl = (boy + boy) * 2

print(f'Петя сделал {boy} журавликов, Сережа - {boy}, a Катя - {girl}')