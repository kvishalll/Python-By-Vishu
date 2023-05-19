# 1.	Write a Python class named Student with two attributes student_id, student_name. 
# Add a new attribute student_class and display the entire attribute and their values of the said class. 
# Now remove the student_name attribute and display the entire attribute with values

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        
    def add_class(self, student_class):
        self.student_class = student_class
        
    def display_attributes(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")
        
    def remove_name(self):
        del self.student_name
# create an instance of the Student class
student1 = Student(2303, "Vishu")

# add the student_class attribute
student1.add_class("Class A")

# display the attributes and their values
student1.display_attributes()


# #To remove the student_name using attribute
# student1.remove_name()
# # display the attributes and their values again
# student1.display_attributes()
