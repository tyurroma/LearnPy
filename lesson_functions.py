#task1
print('Task 1')
def get_summ(one, two, delimiter='&'):
    return str(one.upper()) + str(delimiter) + str(two.upper())

sum_string = get_summ('Learn', 'Python')
print(sum_string)

#task2
print('')
print('Task 2')
def format_price(price):
    price = int(price)
    return 'Price is: {}'.format(price)

display_price = format_price(56.24)
print(display_price)

display_price = format_price(5283768.34865)
print(display_price)