'''
Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя
“Как дела?”, пока он не ответит “Хорошо”. Создайте словарь типа "вопрос": "ответ",
например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее. 
Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в
словаре, программа давала ему соотвествующий ответ.
'''

q_a = {'How are you?': 'Fine', 'What are you doing?': 'Developing'}

def ask_user():
    while True:
        user_text = input('Enter something: ')
        if user_text == 'Good':
            print('Bye!')
            break
        elif user_text in q_a:
            print(q_a.get(user_text))


if __name__ == '__main__':
    ask_user()