'''
Перепишите функцию ask_user() из задания про while, 
чтобы она перехватывала KeyboardInterrupt,
писала пользователю "Пока!" и завершала работу при
помощи оператора break.
'''

q_a = {'How are you?': 'Fine', 'What are you doing?': 'Developing'}

def ask_user():
    try:
            while True:
                user_text = input('Enter something: ')
                if user_text == 'Good':
                    print('Bye!')
                    break
                else:
                    for answer in q_a:
                        if answer == user_text:
                            print(q_a[answer])
                    else:
                        print('You entered: {}'.format(user_text))                        
    except KeyboardInterrupt:
            print(' You pushed Ctrl+C, Bye-bye!')

ask_user()