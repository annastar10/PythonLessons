value = 49200000950000
strval = str(value)
count = 0
for i in strval[::-1]:
    if not i == '0':
        break
    count = count + 1
# print('There total: ', count, ' LAST zeros in this number: ', value)

# zadanie 2
value = 4920000095000
strval = str(value)
count = 0
for i in strval:
    if i == '0':
        count += 1

# print('There total: ', count, ' zeros in this number: ', value)

# zadanie  3a

my_list_1=[1,3,2,4,5]
my_list2=[10,20,15,25,22]
#
#
evenIndexesList = my_list_1[::2] #
oddIndexesList=my_list2[1::2]
my_results_3a =evenIndexesList + oddIndexesList

## zadanie 3b

my_list_1 = [1, 3, 2, 4, 5]
my_list2 = [10, 20, 15, 25, 22]
my_results_3b = [i for i in my_list_1 if i % 2 == 0] +[k for k in my_list2 if not k % 2 == 0]

## zadanie 4
mylist4=[1,2,3,4,5,6]
newList4=mylist4[1::]
newList4.append(mylist4[0])


## zadanie 5
mylist5=[1,2,3,4,5,6]
firstElem = mylist5.pop(0)
mylist5.append(firstElem)

## zadanie 6

random_str6= 'у нас есть некоторая строка из 34 символов 12 отстуствуют и 43 буквы исользованно'
digits = [int(s) for s in random_str6.split() if s.isdigit()]
result5 = sum(digits)

## zadanie 7
random_str7='некотораястрока'
result7=[]
for i in range(0, len(random_str7), 2):
  chars = random_str7[i:i + 2]
  if not len(chars)==2:
      chars+='_'
  result7.append(chars)
result7

# zadanie 8
l_limit='l'
r_limit='r'
stroka8='abcdefghigklmnopqrstuvw'
sub_str=stroka8[stroka8.find(l_limit)+1:stroka8.rfind(r_limit)]

# zadanie 9
l_limit='f'
r_limit='t'
stroka8='abcdefgfhifgklmnoptqrtstuvw' # повторяются символы f и t
sub_str=stroka8[stroka8.find(l_limit)+1:stroka8.rfind(r_limit)]

# zadanie 10

spisokChisel=[2,4,6,2,3,8,5,9,1,4,2,5]
counter=0
dlinaSpiska = len(spisokChisel)-1
for i in range(0, dlinaSpiska):
    if i == 0 or i== dlinaSpiska:
        continue
    prev= spisokChisel[i-1]
    current=spisokChisel[i]
    next=spisokChisel[i+1]
    if prev+next>current:
        counter+=1
print(counter)