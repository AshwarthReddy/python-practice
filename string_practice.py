# Program to display all positions of substring in a given main string

input = 'Life is not measured by the breaths we take, but by the moments that take our breath away. Embrace each day with gratitude, seek growth through challenges, and cherish the people who walk with you. True happiness comes from within, and peace is found in letting go.';
sub = 'i'

flag = False;
n = len(input);
pos = -1;

while True:
   pos =  input.find(sub, pos+1, n)
   if pos == -1:
      break
   print('Found position: ', pos)
   flag = True;
if flag == False:
   print('Not Found')
   
# Counting substring in the given String

print(input.count('is'))
print(input.count('a', 3, 7))

# Replacing a string with another string:

s = 'Learning python is very Easy'
output = s.replace('python', 'DataScience')
print(output)


# Splitting of Strings:

splitString = s.split()
for i in splitString:
   print(i)

dateStr = '17-01-2025'
splitStrDate = dateStr.split('-')
for i in splitStrDate:
   print(i)

t = ['Hello', 'World']
output = '-'.join(t)
print(output)



# Changing case of a String:
print(input.upper())
print(input.lower())
print(input.swapcase())
print(input.title())
print(input.capitalize())

print()

# Checking starting and ending part of the string:

print(input.startswith('life'))
print(input.endswith('go'))




print('your salary is {}, age is {} and city {}'.format(5000, 31, 'Dubai'))
print('Your Salary is {0}, age is {1} and city is {2}'.format(5000, 31, 'Dubai'))
print('Your Salary is {x}, age is {y} and city is {z}'.format(x = 5000, y = 31, z = 'Dubai'))