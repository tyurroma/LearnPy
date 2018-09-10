'''
Напишите функцию get_summ(num_one, num_two),
которая принимает на вход два целых числа (int) и складывает их
Оба акргумента нужно приводить к челому числу при помощи int() 
и перехватывать исключение ValueError если приведение типов не сработало
'''

def get_sum(num_one, num_two):
    return num_one + num_two

while True:
    try:
        num_one = int(input('Enter first num: '))
        num_two = int(input('Enter second num: '))
        result = get_sum(num_one, num_two)
        print(result)
    except ValueError:
        print('Incorrect input format. Please use "int" numbers.')