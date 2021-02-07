import random as rnd


def randCoordinates():
    return {
        'x': rnd.randrange(-10, 10, 1),
        'y': rnd.randrange(-10, 10, 1),
        'z': rnd.randrange(-10, 10, 1),
    }

def addStarsAndPrint(stroka):
    print('***' + stroka + '***')

# zadanie 1
rndList11 = [rnd.randint(0, 100) for v in range(20)]  # 1-i sposob
rndList12 = [rnd.randrange(0, 100, 1) for v in range(20)]  # 2-i sposob

# zadanie 2
triangle = {
    'A': randCoordinates(),
    'B': randCoordinates(),
    'C': randCoordinates(),
}

# zadanie 3
addStarsAndPrint('Some Stroka')

# zadanie 4
persons4 = [
    {'name': 'Vasiliy', 'age': 23},
    {'name': 'Petrovich', 'age': 45},
    {'name': 'Kozlevich', 'age': 17},
    {'name': 'Matrona', 'age': 17},
]
minAge = min(v['age'] for v in persons4)
maxNameLength = max(len(name['name']) for name in persons4)
youngestNamesList = [n['name'] for n in persons4 if n['age'] == minAge]  # a
longestNamesList = [n['name'] for n in persons4 if len(n['name']) == maxNameLength]  # b
avgAge = sum(v['age'] for v in persons4) / len(persons4)  # v
print(youngestNamesList, longestNamesList, avgAge)

# zadanie 5
"""""
5) Даны два словаря my_dict_1 и my_dict_2.
а) Создать список из ключей, которые есть в обоих словарях.
б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
г) Объединить эти два словаря в новый словарь по правилу:
если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
"""""
my_dict_51 = {'A': 'gluh', 'B': 123, 'C': 'S123', 'D': 213}
my_dict_52 = {'L': 'assss', 'K': 23, 'B': 'sda', 'D': 1234}
sameKeys = list(my_dict_51.keys() & my_dict_52.keys())
uniqueKeys = my_dict_51.keys() ^ my_dict_52.keys()
keysInFirstNotInSecond = list(my_dict_51.keys() & uniqueKeys)
newDictFromFirstNotSecondKeys = {key: val for key, val in my_dict_51.items() if key in keysInFirstNotInSecond}

sameKeysWithVals = {key: [my_dict_51.get(key), my_dict_52.get(key)] for key, val in zip(my_dict_51, my_dict_52) if
                    key in sameKeys}
# нас интересуют только уникальные ключи поэтому можно :)
uniqueKeysWithVals = {key: val for key, val in (my_dict_51 | my_dict_52).items() if
                      key in uniqueKeys}  # фильтруем значения по уникальным ключам
result5 = uniqueKeysWithVals | sameKeysWithVals
