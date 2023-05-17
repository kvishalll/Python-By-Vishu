#Simple function 
def print_table():
   i=1
   num=int(input('Enter a number: '))
   while i<=10:
    print(num,' X ',i,' = ',num*i)
    i+=1 
print_table()


# Parameterized function
def print_table(num):
   i=1
   while i<=10:
    print(num,' X ',i,' = ',num*i)
    i+=1
num=int(input('Enter a number: '))
print_table(num)



#Return type with Simple function
def print_table():
   i=1
   table=""
   num=int(input('Enter a number: '))
   while i<=10:
    table+=str(num)+' X '+str(i)+' = '+str(num*i)+'\n'
    i+=1
   return table
print(print_table())


#Return type with Parameterized function 
def print_table(num):
   i=1
   table="" 
   while i<=10:
    table+=str(num)+' X '+str(i)+' = '+str(num*i)+'\n'
    i+=1
   return table
num=int(input('Enter a number: '))
print(print_table(num))

