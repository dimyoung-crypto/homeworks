# Вариант 6. Абитуриенты
import random
from datetime import datetime

# предметы
subjects_in = [{
    'id': '1',
    'name': 'Economy',
    'points': 0,
}, {
    'id': '2',
    'name': 'Mathematic',
    'points': 0,

}, {
    'id': '3',
    'name': 'Sociology',
    'points': 0,

}]

class subject(object):
    def __init__(self, id, name, point):
        self.id = id
        self.name = name
        self.point = point

    def __repr__(self):
        return str({'id': self.id, 'name': self.name, 'points': self.point})

    def __dict__(self):
        return {'id': self.id, 'name': self.name, 'points': self.point}


# рандомные оценки
new_subject = lambda: {i['id']: subject(i['id'], i['name'], random.randint(1, 10)) for i in subjects_in}

# вводные для студентов
students = [{
    'id': 1,
    'last_name': 'Minko',
    'first_name': 'Vasil',
    'surname': 'Vasilevich',
    'home_address': 'Brest',
    'phone_number': '2178394',
    'subjects': new_subject(),

}, {
    'id': 2,
    'last_name': 'Ivanov',
    'first_name': 'Ivan',
    'surname': 'Ivanich',
    'home_address': 'Ivanovo',
    'phone_number': '2657892',
    'subjects': new_subject(),
}, {
    'id': 3,
    'last_name': 'Maksimov',
    'first_name': 'Maksim',
    'surname': 'Maksimovich',
    'home_address': 'Minsk',
    'phone_number': '2888888',
    'subjects': new_subject(),
}, {
    'id': 4,
    'last_name': 'Zubko',
    'first_name': 'Alena',
    'surname': 'Vitalevna',
    'home_address': 'Los-Angeles',
    'phone_number': '2110098',
    'subjects': new_subject(),
}]

class abiturient(object):
    def __init__(self, id, last_name, first_name, surname, home_address,phone_number, subjects):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.surname = surname
        self.home_address = home_address
        self.phone_number = phone_number
        self.subjects = subjects

    def __repr__(self):
        return str({'id': self.id,
                    'last_name': self.last_name,
                    'first_name': self.first_name,
                    'surname': self.surname,
                    'home_address': self.home_address,
                    'phone_number': self.phone_number,
                    'subjects': self.subjects})

    def __dict__(self):
        return {'id': self.id,
                'last_name': self.last_name,
                'first_name': self.first_name,
                'surname': self.surname,
                'home_address': self.home_address,
                'phone_number': self.phone_number,
                'subjects': self.subjects}

abiturients = [abiturient(i['id'], i['last_name'], i['first_name'], i['surname'],
                   i['home_address'], i['phone_number'],
                   i['subjects']) for i in students]

for e in abiturients:
    print(e.subjects)
    ##print("Full points about entran:\n" +e.last_name+ " Economy" +)

'''
print('\n\n')
# сортировка по оценкам за физику id:'2'
for e in abiturients:
    print(e.subjects)

print()
abiturients.sort(key=lambda x: x.subjects['2'].point)

for e in abiturients:
    print(e.subjects)
'''