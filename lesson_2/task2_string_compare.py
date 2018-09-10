'''
Написать функцию, которая принимает на вход две строки
Проверить, является ли то что переданно функции строками. Если нет - вернуть 0
Если строки одинаковые, верунть 1
Если строки разные и первая длиннее, вернуть 2
Если строки разные и вторая строка 'learn', возвращает 3
Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты
'''

def compare(str1, str2):
    if str1.isdigit() == True and str2.isdigit() == True:
        return 0
    if str1 == str2:
        return 1
    else:
        if len(str1) > len(str2):
            return 2
        elif str2 == 'learn':
            return 3


test1 = compare('str1', 'str1')
print(test1)
test2 = compare('ghdbtnsadsdf', 'str23sd')
print(test2)
test3 = compare('1', '2')
print(test3)
test4 = compare('learn', 'learn')
print(test4)
test5 = compare('py', 'learn')
print(test5)