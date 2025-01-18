# 1. Creation of List Objects:

list = []
print(list)
print(type(list))

# 2.  if we know the elements

list = [100, 200, 300, 400]

print(list)

# dynamic inputs 

# list = eval(input('please enter the list :'))
# print(list)

# # 4. With list() function:
# list = list(range(0, 20))
# print(list)

# 5. with split() function:
input = 'Learnig python is very easy';
list = input.split();
print(list)


# Accessing elements of List:
#  1. by using index

print(list[0])
print(list[-1])

# 2. By using slice operator:
print(list[1:2:2])
print(list[2::2])


# itarating the elements

n=[0,1,2,3,4,5,6,7,8,9,10]
length = 0;
while length< len(n):
    print(n[length])
    length = length+1;


print()
# By using loop
for i in n:
    print(i)

print()
# 3. To display only even numbers:

for i in n:
    if i%2 == 0:
        print(i)

# To display elements by index wise:

# list = ['A', 'B', 'C', 'D']

# length = len(list)

# for i in list(range(length)):
#     print('index = {} & value is ='.format(i, list[i]))



# Important functions of List:

# len():
print(len(list))

print()
# count()
print(list.count(1))


print()

# index()

print(n.index(5))

# II. Manipulating elements of List:
#  append()
# insert()
# extend()
# remove()
# pop()

n.append(100)
print(n)
n.insert(0, 200)
print(n)
odds = [1, 3, 5, 9]
n.extend(odds)
print(n)
n.remove(200)
print(n)
n.pop(1)
print(n)

# Ordering elements of List:
# reversee()
# sort()
# 

list = [1, 2, 9, 3, 2, 6, 8, 9];

print(list.sort())
print()

print(list.reverse())
print()
print(list.sort(reverse=True))


print(list(range(2)))