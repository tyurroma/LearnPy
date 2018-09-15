import csv

list_of_dict = [
                {'name': 'Masha', 'age': 25, 'job': 'Scientist', 'salary': 170000}, 
                {'name': 'Vasya', 'age': 8, 'job': 'Programmer'}, 
                {'name': 'Edouard', 'age': 48, 'job': 'Big boss'},
                ]

def csv_generator(list_of_dict):
    try:
        with open('export.csv', 'w', encoding='utf-8') as myfile:
            fields = ['name', 'age', 'job']
            writer = csv.DictWriter(myfile, fields, delimiter=',')
            writer.writeheader()
            for user in list_of_dict:
                writer.writerow(user)
    except ValueError:
        print('Dict contains fields not in fieldnames!')


if __name__ == '__main__':
    csv_generator(list_of_dict)