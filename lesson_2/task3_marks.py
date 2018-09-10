'''
Создать список с оценками учеников разных классов школы вида 
[{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
'''

school = [{'school_class': '1a', 'scores': [3,4,4,5,2]}, 
        {'school_class': '1b', 'scores': [5,5,5,5,2]}, 
        {'school_class': '1c', 'scores': [3,4,4,5,2]}, 
        {'school_class': '1d', 'scores': [5,3,5,5,2]}, 
        {'school_class': '1e', 'scores': [3,3,2,5,2]}, 
        ]

classes_count = 0
sum_avg_score = 0
school_avg_score = 0

for classes in school:
    classes_count += 1
    for score in classes:
        score = classes['scores']
        avg_score = sum(score) / len(score)
    sum_avg_score += avg_score
    print('{} has average score {}'.format(classes['school_class'], avg_score))
school_avg_score = sum_avg_score / classes_count

print('Entire school has average score {}'.format(school_avg_score))