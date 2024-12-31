from datetime import datetime, timedelta;
from array import array
# import helprs;
from helpers import wishYouHappyNew

# name = input('What is your name ....?')
# print('Hello ' + name)
# print('Hello ' + name)
# print('Hello ')

firstName = 'ANR'
lastName = 'Bhupathi'

# output = 'Hello ' + firstName + ' ' + lastName
output = f'Hello {firstName} {lastName}'
output = 'Hello {} {}'.format(firstName, lastName)
output = 'Hello {1} {0}'.format(firstName, lastName)

# print(output)


# DATA TYPES 
# firstNumber  = 10;
# secondNumber = 20;

# # print(firstNumber ** secondNumber)
# firstNumber = input('Enter first number: ')
# secondNumber = input('Enter second number: ')

# print(int(firstNumber) ** int(secondNumber))

# total_days_in__feb = 28;
# print('Total days in feb: ' + str(total_days_in__feb))


today = datetime.now();

# print('Today is : ' +str(today))

# print('Day: ' + str(today.day))

oneDay = timedelta(days=1);

yesterDay = today - oneDay;

# print('Yesterday was: '+ str(yesterDay));

oneWeek = timedelta(weeks=1);
lastWeek = today - oneWeek;
# print('last week was: '+ str(lastWeek))


# birthDay = input('please tell me your Birthday: dd/mm/yyyy');

# birtDate = datetime.strptime(birthDay, '%d/%m/%Y')

# print('Your BirthDay is: ' + str(birtDate))



# ERROR HANDLING

x = 100
y = 0


# print(x/y)

# try:
#     print('This is a try block')
#     print(x/y)
# except ZeroDivisionError as e:
#     print('You cannot divide by zero');
# else:
#     print('Division was successful')
# finally:    
#     print('This will always run')


# CONDITIONAL STATEMENTS

# salary = 100000;

# if int(salary) > 10000:
#     print('You are rich')
# else:  
#     print('You are poor')

# country = input('Enter your country: ');

# if country.capitalize() == 'INDIA':
#     print('You are an Indian')
# else: 
#     print('You are not an Indian')


# salary = input('Enter your salary in lakhs: ');
# tax = 0;

# if int(salary) >= 20 or int(salary) >= 30:
#     areYouNRI  = input('are you NRI ...?')
#     if areYouNRI == 'yes':
#         print('You are NRI, no tax applicable')
#     else:
#         print('your tax is 30%')
# elif int(salary) == '20':
#     print('your tax is 20%')
# elif int(salary) == '10':
#     print('your tax is 10%')
# else:
#     print('no tax applied')
    
# COLLECTIONS

chris = {};

chris['firstName'] = "Krish"
chris['lastName'] = "Bhupathi"

josh = {};
josh['firstName'] = "Josh"
josh['lastName'] = "Bhupathi"

print(chris);
print(josh)

people = [];

people.append(chris);
people.append(josh);

print(people)


people.append({'first': 'ANR', 'last': 'Bhupathi'});

print(people)


peoples = ['ANR', 'Krish', 'Josh', 'Bhupathi'];

for person in peoples:
    print(person)


print()

index = 0;
while index < len(peoples):
    print(peoples[index])
    index = index + 1


#  FUNCTIONS
def greet(name):
    return 'Hello ' + name;


print(greet('ANR'));


def getFullName(firstName, lastName = 'Bhupathi'):
    return f"{firstName} {lastName}";


print(getFullName('ANR'));

squere = lambda x: x * x;
fullName = lambda firstName, lastName = "Bhupathi": f"{firstName} {lastName}";

print(squere(10));
print(fullName('ANR'))


# print(helprs.getName())

print(wishYouHappyNew())


