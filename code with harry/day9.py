print("---------------------------------------day9----------------------------------------------")
print("-----------------------------------Typecasting-------------------------------------------")

'''
=> The conversion of one datatype into other datatype is called typecasting or type conversion
=> herre we will use str(), ord(), tuple(), set(), etc

=> There are two type of type casting
   1) Explicit convrsion :
      The conversion of one data type into another datatype, done via developer or 
      programmer's intervation or manually as per the requirent is called expicit type conversion
   2) Impicit conversion : 
       according to the level one data type is converted into another by python automatically is called Implicit 
'''

'''
a=1
b=2
print(a+b)
'''

a="1"
b="3"
print(a+b) #output 13 but we want 4 as output
print(int(a) + int(b))

#-----Example of explicit typecasting
print("-----Example of explicit typecasting------")
string = "15"
number = 7
string_num = int(string) #throws an error if the string is not valid integer

sum = number + string_num
print("The sum of both the number is : ", sum)

print("\n-----Example of Implicit typecasting")

#python will automatically convert a into int

a = 7
print(a)
print(type(a))

#python will automatically convert b into float

b =0.9
print(b)
print(type(b))

# bpython will automatically convert c into float as it is float addition
c = a+b
print(c)
print(type(c))