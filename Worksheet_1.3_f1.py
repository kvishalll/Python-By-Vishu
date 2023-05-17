# #Simple function 
pi=22.0/7 
def area():
   i=1
   while i<=10:
    r=int(input("Enter radius of circle ")) 
    print('area of circle with radius ',r,' units is ',pi*r**2,' sq units')
    i+=1
area()



# # Parameterized function
pi=22.0/7
def area(r):
   print('area of circle with radius ',r,' units is ',pi*r**2,' sq units')
i=1
while i<=10:
    r=int(input("Enter radius of circle "))
    area(r)
    i+=1


# #Return type with Simple function
pi=22.0/7
def area():
   r=int(input("Enter radius of circle "))
   result=''
   i=1
   while i<=10:
    result+='area of circle with radius '+str(r)+' units is '+str(pi*r**1)+' sq units'+'\n'
    i+=1
    return result
print(area())


#Return type with Parameterized function
pi=22.0/7
def area(r):
   result=pi*r**2
   return result

i=1
while i<=10:
   r=int(input("Enter radius of circle "))
   print('area of circle with radius ',r,' units is ',area(r),' sq units')
   i+=1
