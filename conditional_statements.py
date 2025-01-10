a,b,c = 30, 20, 15 ;


minValue = a if a<b else b;
print(minValue)


# min = None;
# if a < b and a < c:
#     min = a
# elif b < c:
#     min = b;
# else:
#     min = c;
# print(min)

#  minValue1 = a if a < b and a < c else b if b < c else c
# print(minValue1)

max1=a if a>b and a>c else b if b>c else c

minValue1 = min(a, b, c)
print(minValue1)

if a < b and a < c:
    minimum_value = a
elif b < c:
    minimum_value = b
else:
    minimum_value = c

# Displaying the result
print("The minimum value is:", minimum_value)

print(max1)


a = True;
# True = 1
b = False;
# False = 0
print(a>b)


first_name = "Aswarthana";
last_name = "Reddy"
print(first_name > last_name)



n1 = 5;
for i in range(1, n1+1):
    for j in range(1, i+1):
        print("* ", end = "")
    print()


print()
print()
print()

n = 6

for i in range(1, n + 1):
    print("* " * i)


print()
print()
print()

p = 5;
for i in range(1, p + 1):
    print(" " * (p - i), end = "")
    print("* " * i)







