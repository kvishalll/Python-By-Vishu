class students:

	attr1 = "Vishu"
	attr2 = "Raj"

	def fun(self):
		print("I'm ", self.attr1)
		print("I'm ", self.attr2)


name = students()

print(name.attr1)
name.fun()


# class Employee:    
#     id = 2303   
#     name = "Vishu"    
#     def display (self):    
#         print("ID: %d \nName: %s"%(self.id,self.name))    
# # Creating a emp instance of Employee class  
# emp = Employee()    
# emp.display()    



# class Bike:
#     name = ""
#     gear = 0

# bike1 = Bike()

# bike1.gear = 11
# bike1.name = "Mountain Bike"

# print(f"Name: {bike1.name}, Gears: {bike1.gear} ")