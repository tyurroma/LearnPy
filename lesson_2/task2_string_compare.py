'''
Написать функцию, которая принимает на вход две строки
Проверить, является ли то что переданно функции строками. Если нет - вернуть 0
Если строки одинаковые, верунть 1
Если строки разные и первая длиннее, вернуть 2
Если строки разные и вторая строка 'learn', возвращает 3
Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты
'''

def compare(str1, str2):
    if isinstance(str1, str) == False or isinstance(str2, str) == False:
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str2 == 'learn':
        return 3
    else:
        return 'nothing'
if __name__ == '__main__':
    test1 = compare('str1', 1)
    print(test1)
    test2 = compare('ghdbtnsadsdf', 'str23sd')
    print(test2)
    test3 = compare('sdf1', '2slajhbf')
    print(test3)
    test4 = compare('learn', 'learn')
    print(test4)
    test5 = compare('py', 'learn')
    print(test5)