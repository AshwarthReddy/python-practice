f = open('abc.txt', 'a')

# f.write('Amma\n')
# f.write('Nanna\n')
# f.write('Haadya\n')
# print('Data written the file successfully')
# f.close()


names = ['\n', 'Priya\n', 'Haadya\n', 'Ayaan\n']
f.writelines(names)
print('List of lines written successfully')
f.close();

read_file = open('abc.txt', 'r')

data = read_file.read();
print(data)
read_file.close();

print('###############################')
read_file1  = open('abc.txt', 'r')
data1 = read_file1.read(10);
print(data1)
read_file1.close();

print('###############################')

read_file_by_lines = open('abc.txt', 'r');
data3 = read_file_by_lines.readlines();
print(data3)
read_file_by_lines.close();

print('###############################')

read_file_lines = open('abc.txt');
data3 = read_file_lines.readlines();

print('###############################')
for i in data3:
    print(i)

read_file_lines.close();


with open('abc.txt', 'w') as f4:
    f4.write('Suseela\n');
    f4.write('Appireddy\n');
print('is file is closed ? ', f4.closed)
print('write operation completed successfully')

import os, sys;

is_file_exists = os.path.isfile('abcd.txt')
print('is abcd file exists', is_file_exists)

is_file_exists = os.path.isfile('abc.txt')
print('is abc file exists', is_file_exists)


image_file = open('/Users/aswarthana/Downloads/Sundar_Pichai_-_2023.jpg', 'rb');
write_image = open('/Users/aswarthana/Downloads/Sundar_Pichai_-_2023_updated.jpg', 'wb');

bytes = image_file.read();
write_image.write(bytes)
print('new image copied successfully')