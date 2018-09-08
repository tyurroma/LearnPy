def format_price(price):
    price = int(price)
    return 'Price is: {}'.format(price)

display_price = format_price(56.24)
print(display_price)

display_price = format_price(5283768.34865)
print(display_price)