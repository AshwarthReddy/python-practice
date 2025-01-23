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
