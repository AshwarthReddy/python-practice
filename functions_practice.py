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





