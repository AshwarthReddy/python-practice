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


# print(list(range(2)))


# TUPLE DATA STRUCTURE
#  tuple creation
# 1. empty
t = ();
print(type(t))

t1 = 10,
print(type(t1))

t2 = 10, 20, 30, 40, 90
print(type(t2))

# min & max functions

print(min(t2))
print(max(t1))

#  Tuple Packing and Unpacking:

a = 10,
b = 20,
c = 30,
d = 40

t4 = a,b,c,d
print(t4)
print(type(t4))

t5 = 10, 20, 30, 40
a, b, c, d = t5;
print(a)

# write a program to sum of tuple

t6 = 10, 20, 30, 40, 50, 60, 70, 80

sum = 0;
for i in t6:
    sum = sum+i;

print(sum)

#  SET data structure
#  set creation ways

s = {10, 20, 30, 40, 60, 45, 76, 22}
print(type(s))
print(s)

l = [10, 20, 30, 40, 60, 45, 76, 22]
s1 = set(l)
print(type(s1))
print(s1)

s2 = set(range(10))

print(type(s2))
print(s2)


# Dictionary

d = {};
d1 = dict();
d3 = {100: 'ANR', 200: 'Bhupathi', 300: 'Reddy'}
print(type(d))
print(type(d1))

d[100] = 'Shiva';
d[200] = 'Senkar';
d[300] = 'Prabha';
d[400] = 'Prashanthi'

print(d)
print(d3)
print(d3[100])

del d3[300]
print(d3)
d3.clear()
print(d3)

d4 = dict([(100, 'durga'), (200, 'shiva'), (300,'Prabha')])
# t6 = tuple(200,300, 500);
# t7 = tuple('ANR', 'OM', 'Shiva')
# print(d4)
# d5 = dict(t6, t7)
# print(d5)

print(len(d4))

print(d4.get(500, 'Priya'))

d4.pop(300)

print(d4)
d4.popitem()
print(d4)

print(d4.keys())
print(d4.values())

for k,v in d3.items():
    print(k ,'-',v)

d5 = d3.copy()
print(d5)
d5.setdefault(100, 'Haadya')
print(d5)

d5.update(d3)
print(d5)