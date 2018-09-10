'''
Попросить пользователя ввести возраст при помощи input и положить результат в переменную.
Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
учиться в детском саду, школе, ВУЗе или работать.
Вызвать функцию, передав ей возраст пользователя и положить результат работы функции
в преременную. Вывести содержимое переменной на экран
'''

def definition(age):
    if 3 <= age <= 6:
        print('Go to a kindergarten')
    elif 7 <= age <= 18:
        print('Go to a school')
    elif 18 <= age <= 23:
        print('Go to a university')
    elif 23 <= age <= 60:
        print('Go to a work')
    elif 60 <= age <= 116:
        print('Retired')
    elif age > 116:
        print('Death')
    else:
        print('You are too young for kindergarten')

age = int(input('Enter your age: '))
definition(age)
