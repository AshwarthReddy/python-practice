class Student:
    ''' this student class'''

    def __init__(self, id, name,  email):
        self.id = id
        self.name = name;
        self.email = email

    def get_student_deails(self):
     print('Student Details is id : {} name : {}  email : {}'.format(self.id, self.name, self.email));

s = Student(100, 'Nanna', 'nanna@gmail.com');

s.get_student_deails();

