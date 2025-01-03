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






