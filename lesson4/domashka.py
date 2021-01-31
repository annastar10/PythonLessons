# Zadanie N1

my_list = [1,2,3,45,80, 100, 160,200]
for x in my_list:
    if x>100:
     print(x)
# Zadanie 2

my_list = [1,2,3,45,80, 100, 160,200]
my_results=[]
for x in my_list:
    if x>100:
     my_results.append(x)
print(my_results)
# Zadanie 3

my_list = [1,2,3,45,80, 100, 160,200]
if len(my_list)<=2:
    my_list.append(0)
elif len((my_list))>=2:
  lastItem=my_list[-1]
  pre_last_item=my_list[-2]
  my_list.append(lastItem + pre_last_item)
    # print(my_list)
print(my_list)

# Zadanie 5

my_indexes = [0,1,2,3,4]
my_list=['dirt',7,8,34,700]
for my_index in my_indexes:
    print(my_list[my_index])


# Zadanie 6

my_list1=[0,1,2,3,4]
my_list2=['dirt',7,8,34,700]
for x in my_list1:
    val = my_list2[x]
    print(x,val)

# Zadanie 7

my_string = '0123456789'
res=[]
for decimal in my_string:
    for unit in my_string:
        number = int(decimal + unit)
        res.append(number)

print(res)