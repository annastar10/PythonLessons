my_tuple = (1,2,3, "twenty", True, (1,2),"twenty")
print(type(my_tuple))

print(my_tuple)
print(my_tuple[::-2])
print(my_tuple[-1][-1])
for value in my_tuple:
    print(value)
    my_tuple.index(3)
print(my_tuple.index("twenty",6))
print(my_tuple.count(8))
a=2
b=3

# tmp=a
# a=b
# b=tmp
a,b = b, a
print(a,b)

