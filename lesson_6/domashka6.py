# https://github.com/30nt/IntroPython_14_01/blob/main/Homeworks/lesson6.txt

# zadani 1

myList1 = ['qwerty', 'asdfg', 'zxcvb', 'poiuy', 'mnbvc']
resultList1 = []
for key, value in enumerate(myList1):
    if key % 2 == 0:
        resultList1.insert(key, value)
    else:
        resultList1.insert(key, value[::-1])

# zadanie2
myList2 = ['qwerty', 'asdfg', 'zxcvb', 'poiuy', 'amnbvc']
result2 = [v for v in myList2 if v.startswith('a')]

# zadanie 3
myList3 = ['qwerty', 'asdfg', 'zxcvb', 'poiuy', 'mnabvc', 'kjhgfrt', 'bgfgvgakjh']
result3 = [v for v in myList3 if 'a' in v]

# zadanie 4
myList4 = ['qwerty', 2, 'asdfg', 4, 'zxcvb', 'poiuy', 10, 'amnbvc']
result4 = [v for v in myList4 if type(v) is str]

# zadanie 5
myString5 = 'qwertyqt'
duplChars = [v for v in myString5 if myString5.count(v) > 1]
result5 = list(dict.fromkeys(duplChars))

# zadanie 6
myString61 = 'qwerty'
myString62 = 'tpoiuyt'
duplChars = [v for v in myString61 + myString62 if myString61.count(v) > 0 and myString62.count(v) > 0]
result6 = list(dict.fromkeys(duplChars))

# zadanie 7
myString71 = 'qwerty'
myString72 = 'tpoiuyt'
duplChars = [v for v in myString61 + myString62 if myString71.count(v) == 1 and myString72.count(v) == 1]
result7 = list(dict.fromkeys(duplChars))

# zadanie 8
slovar8 = {
    'Фамилия': 'Ivanov',
    'Имя': 'Ivan',
    'Возраст': 35,
    'Проживание': {
        'Страна': 'Ukraina',
        'Город': 'Zmerenka',
        'Улица': 'Pervomayskaya'
    },
    'Работа': {
        'Наличие': 'est',
        'Должность': 'PerviyKudaPoyti'
    }
}

# zaadanie 9
dictionary9 = {
    'Составляющие': {
        'Коржи': {
            'Мука': 200,
            'Молоко': 123,
            'Масло': 34,
            'Яйцо': 67
        },
        'Крем': {
            'Сахар': 123,
            'Масло': 32,
            'Ваниль': 54,
            'Сметана': 43
        },
        'Глазурь': {
            'Какао': 10,
            'Сахар': 12,
            'Масло': 5,
        }
    }
}
