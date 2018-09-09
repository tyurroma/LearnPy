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
