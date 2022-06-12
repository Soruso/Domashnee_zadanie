tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

def gen():
    bolshee = max(len(tutors), len(klasses))
    for i in range(bolshee):
        if i + 1 > len(tutors):
            ls = ('None', klasses[i])
        elif i + 1 > len(klasses):
            ls = (tutors[i], 'None')
        else:
            ls = (tutors[i], klasses[i])
        yield ls

g = gen()

while True:
    print(next(g))