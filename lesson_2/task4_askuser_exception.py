'''
Перепишите функцию ask_user() из задания про while, 
чтобы она перехватывала KeyboardInterrupt,
писала пользователю "Пока!" и завершала работу при
помощи оператора break.
'''

q_a = {'How are you?': 'Fine', 'What are you doing?': 'Developing'}

def ask_user():
    while True:
        try:
            user_text = input('Enter something: ')
            if user_text == 'Good':
                print('Bye!')
                break
            elif user_text in q_a:
                print(q_a.get(user_text))
        except KeyboardInterrupt:
            print('\nYou pushed Ctrl+C, Bye-bye!')
            break
            

if __name__ == '__main__':
    ask_user()