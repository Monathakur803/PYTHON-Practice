print("-------------------------------------------------------------------------------------------------------------------------------")
print("                                                                Day 21                         ")
print("                                                           Function Arguments                  ")
print("-------------------------------------------------------------------------------------------------------------------------------")
print()
'''
There are four type of arguments that we can provide in a function:
:) Default Argument:
               We can pronide a default value while creating a function.This way the function assumes a default values
               is not provided in the function call for that argument.
:) Keyword Argument:
               We can provide arg with key= value, this way the interprater recognizes the arg by the parameter name.
               Hence, the  the order in which the argument are  passed does not matter.
:) Variable length Argument:
               Sometime we may need to pass more argument than tose defined in actual function.
               This can be done using variable-length argument.
:) Required argument:  
               In case we don't pass arg with a key=value syntax, then it is necessery to pass
               the arg in correct position order and the number of argument passed should match with
               actual function defination 
'''
print("Here's the example of Required argument:")
def avg(a,b):
   print("The average is: ",(a+b)/2)
   
avg(23,2)

print("Here's the example of Default argument:")
def avg(a=4,b=6):
   print("The average is: ",(a+b)/2)
   
avg( )
avg(12,2) #when we will provide argument then it will ignore default arg .
avg(4) #here a=4 where value of b is take by default from function.
avg(b=4)#here b=4 where value of a is take by default from function.
print()
def name(f_name,m_name="Ranjeet", l_name="Thakur"):
   print("Hello,", f_name,m_name,l_name)
name("Mona")
name("Pushpa")
name("Jayesh")
name("Pooja","Kumari","Sharma")
print()

print("Here's the example of Default argument:")
def avg(a=3,b=3):
   print("The average is: ",(a+b)/2)
   
avg(a=23,b=2)
avg(a=12,b=2)
avg(b=2)
print()


print("Here's the example of Require argument:")
def avg(a,b,c=3):
   print("The average is: ",(a+b+c)/3)
#avg(b=3) #here it id=s necesary to gie valur of a as we have not provided in fumction, so it will generate error
avg(6,3)#these value will be provided to a and b 
print()

print("Here's the example of Variable length Argument:")
#Here we will take argument as tupple.
def avg(*num):
   #print(type(num)) #Num is kinde of tupple
   sum = 0
   for i in num:
      sum = sum + i
   print("The average is: ", sum/len(num))
# Here we can provide multiple argument as per requirement.
avg(3,4,5) 
avg(1,2)
avg(1,2,3,2)
print()

print("Eample, taking arg as dictonary:")
def name(**name):
   print(type(name))
   print("Hello,", 
         name["fname"],
         name["mname"],
         name["lname"]
         )
name(mname="Kumari",
     lname ="Thakur",
     fname = "Pooja"
     )
print()
# Return Statement:
# Return statement  is used to return the value of the expression back to the calling function.

print("Example of return statement")
def avg(*num):
   sum = 0
   for i in num:
      sum = sum + i
  # print("The average is: ", sum/len(num))
   return sum/len(num) #if we will not return than it will give none value
c = avg(4,4,2,6) #calling function
print(c)
   