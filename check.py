class Student:
    pass

class Marks:
    pass

# create instances of the Student and Marks classes
student1 = Student()
student2 = Student()
marks1 = Marks()
marks2 = Marks()

# check if the instances are of the respective classes
print(isinstance(student1, Student))
print(isinstance(student2, Student))
print(isinstance(marks1, Marks))
print(isinstance(marks2, Marks))

# check if the classes are subclasses of the object class
print(issubclass(Student, object))
print(issubclass(Marks, object))