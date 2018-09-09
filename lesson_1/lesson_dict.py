#task1
print('Task 1')
D = {'City': 'Moscow', 'Temperature': 20}
print(D['City'])
D['Temperature'] = 15
print(D)

#task2
print(' ')
print('Task 2')
print(D.get('Country', 'Russia'))
D['Date'] = '9.08.2018'
print(D)
print(len(D))