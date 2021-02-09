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
result2 = [s for s in myList2 if s.startswith('a')]

# zadanie 3
myList3 = ['qwerty', 'asdfg', 'zxcvb', 'poiuy', 'mnabvc', 'kjhgfrt', 'bgfgvgakjh']
filter_by_char3 = [s for s in myList3 if 'a' in s]

# zadanie 4
myList4 = ['qwerty', 2, 'asdfg', 4, 'zxcvb', 'poiuy', 10, 'amnbvc']
only_strings_list4 = [s for s in myList4 if type(s) is str]

# zadanie 5
myString5 = 'qwertyqt'
remove_dupl_chars5 = list(set(myString5))

# zadanie 6
myString61 = 'qwerty'
myString62 = 'tpoiuyt'
same_chr_in_both6 = [ch for ch in set(myString61).union(set(myString62)) if
                     (ch in set(myString61)) and (ch in set(myString62))]

# zadanie 7
myString71 = 'qwerty'
myString72 = 'tpoiuyt'
once_occur_in_both = [chr for chr in set(myString72).union(set(myString71)) if
                      myString71.count(chr) == 1 and myString72.count(chr) == 1]
print(once_occur_in_both)

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
