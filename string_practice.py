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




# . Write a program to sort the characters of the string and first alphabet symbolsfollowed by numeric values
s = 'B4A1D3'

s1=s2=output=''

for i in s:
   if i.isalpha():
      s1 = s1+i;
   else:
      s2 = s2+i;

for i in sorted(s1):
   output = output+i;

for i in sorted(s2):
   output = output + i;


print(output)

'''
Write a program for the following requirement
input = a4b3c2
output = aaaabbbcc
'''

# Write a program for the following requirement 
# 

input1 = 'a4b3c2'
output1 = ''
for i in input1:
   if i.isalpha():
      output1 = output1+i;
      previous = i;
   else:
    output1 =  output1 + previous*(int(i)-1)

print(output1)



'''
Write a program to remove duplicate characters from the given input string?
'''

input2 = 'ABCDABBCDABBBCCCDDEEEF'
l = [];

for i in input2:
   if i not in l:
      l.append(i);

output3 = ''.join(l);

print(output3)

'''
Write a program to find the number of occurrences of each character present in the
given String?
'''


input4 = 'ABCABCABBCDE';
d = {};

for i in input4:
   if i in d.keys():
      d[i] = d[i]+1
   else:
      d[i]= 1;

for k, v in d.items():
   print('{} = {} Times'.format(k, v))