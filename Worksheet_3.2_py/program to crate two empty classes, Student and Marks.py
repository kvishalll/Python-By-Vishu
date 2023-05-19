# 5.	Write a Python program to crate two empty classes, Student and Marks. 
# Now create some instances and check whether they are instances of the said classes or not. 
# Also, check whether the said classes are subclasses of the built-in object class or not

# define the Student class
class Student:
    pass

# define the Marks class
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