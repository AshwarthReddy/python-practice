def squrt(num):
    result = 0;
    if num == 0:
      return None;
    while num >= 1:
        result = result*num
        num = num-1;
    return result;


def get_first_name_and_last_name(firstName, lastName):
   return firstName, lastName;


print(squrt(5))
print(get_first_name_and_last_name(firstName='Ashwarth', lastName='Reddy'))




def factorial(number):
  if number == 0:
    result = 1;
  else: 
    result = number * factorial(number-1)
  return result;

print(factorial(5))


#  Anonymous Functions or lambda functions

s = lambda n: n*n;

print('the squre of 4 is :', s(4))
print('the squre of 5 is :', s(5))

sum = lambda n : n+n;
print('the sum of 2 is :', sum(2))
print('the sum of 100 is :', sum(100))

sum_of_two_numbers = lambda a,b: a+b;
print('the sum of 100, 300 is :', sum_of_two_numbers(100, 300))
print('the sum of 100, 600 is :', sum_of_two_numbers(100, 600))


biggest_no = lambda a,b: a if a > b else b;

print('the bigger no of 100, 600 is :', biggest_no(100, 600))
print('the bigger no of 999999, 66666666 is :', biggest_no(999999, 66666666))


def isEven(number):
  if number % 2 ==0:
    return True;
  else: return False;


numbers = [100, 2000, 299, 444, 999, 222];
even_numbers = list(filter(isEven, numbers));
print(even_numbers)

odd_numbers = list(filter(lambda x:x%2 !=0, numbers))
print(odd_numbers)

squer_numbers = list(map(lambda x:x*2, numbers))
print(squer_numbers)

from functools import reduce;

total_sum = reduce(lambda x,y: x+y, numbers);
print(total_sum)

sum_of_two_hundreds = reduce(lambda x,y:x+y, range(1, 200));
print(sum_of_two_hundreds)

# Function Aliasing

def greet(name):
  print('Good Evening', name);

greet('Ganeshaya')

wish = greet;
wish('OM')

del greet;

wish('Amma')


#  Generators

def myGen():
  yield 'A';
  yield 'B';
  yield 'C';

g = myGen();
print(type(g))
print(next(g))
print(next(g))
# print(next(g))
# print(next(g))

def countDown(num):
  print('countDown start')
  while num>0:
    yield num;
    num = num-1;

values = countDown(5)

for x in values:
  print(x)

print()

def generate_first_n_numbers(num):
  n = 1;
  while n<num:
    yield n;
    n = n+1;


values = generate_first_n_numbers(10)

# for i in values:
#   print(i)

nums = list(values)
print(nums)



