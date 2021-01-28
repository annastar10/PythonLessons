# zadanie 1
# variant 1
my_value = 234
if my_value < 100:
    new_val = my_value/2
else:
 new_val=234*-1

print(new_val)

# variant 2
x = 234
new_x = x/2 if x<100 else x*-1
print("Pervoe zadanie: ", new_x)

# zadanie 2

value_2=199

new_val2= 1 if value_2<100 else 0

print("Vtoroe zadanie: ", new_val2)

#  zadanie 3

value_3=199

new_val3= True if value_3<100 else False
print("tretiy vopros: ", new_val3)

# zadanie 4

my_string4 = "malenkieBOLSHIE"
print("Zadanie 4 menyaem registr na bolshie: ",my_string4.upper())

# zadanie 5
my_string5 = "malenkieBOLSHIE"
print("Zadanie 5 menyaem vse na nizniy regiistr: ", my_string5.lower())

# zadanie 6

my_string6 = "abcd"
my_string6 = my_string6+my_string6 if len(my_string6)<5 else my_string6
print("Zadanie 6 dopisivaem stroku: ",my_string6 )

# zadanie 7

my_string7 = "abcd"
my_string7 = my_string7+my_string7[::-1] if len(my_string7)<5 else my_string7
print("Zadanie 7 dopisivaem stroku: ",my_string7 )

# zadanie 8

my_string8="s123dhjh jkh ^* (*&^ sdhsadhj"

my_string8="".join(s for s in my_string8 if s.isalnum()  )
print("zadanie 8 vivodim alphanum: ", my_string8)

# zadanie 9
my_string9="sdhjh   123jkh ^* ( *&^ sdhsadhj"

my_new_string9="".join(s for s in my_string9 if  not s.isalnum())
print("zadanie 9 vivodim not alphanum: ", my_new_string9)

# zadanie 10

my_string10="s123dhjh jkh ^* (*&^ sdhsadhj"

my_string10="".join(s for s in my_string10 if not s.isalnum() and s!= " ")
print("zadanie 10 vivodim not alphanum and not space: ", my_string10)
