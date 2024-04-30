print("--------------------------------------------------------------------day13------------------------------------------------------------")
print("----------------------------------------------------------string method in python----------------------------------------------------")

#strings are immutable i.e we cann't change it

a = "Mona"
print(a)
print("length is : ",len(a))
print("Uppercase : ",a.upper())
print("Lowercase: ",a.lower())
b = "Pooja Thakur.. .. ..."
print("\n","Another string :", b)
print("After striping . in above string: ",b.rstrip("."))

print("Replacing Thaakur with Sharma : ",b.replace("Thakur","Sharma"))

print(b.split("."))

blogHeading = "introduction to pYtHon"
print("\n",blogHeading.capitalize()) #captilize method turns only first char of string to uppercase and rest of caracter turned into lowercase automatically. 
print()

#center method aligns the stirng to the center as per parameters given by the user.

str = "Welcome the the console"
print(str)
print("Length",len(str))
print(str.center(50))
print("After alligning length is :",len(str.center(50)))
print()
x ="!!!Mona!!!Mona !! !Mona"
print(x)
print("Count no.  of occurance of mona in above string: \n",x.count("Mona"))
print()

#endwith() method check if the string end with a given value. If yes then return True, else False.
y = "Welcome to Vrindawan!!!!!!!!!"

print("Does the above stirng ends with '!' : \n",y.endswith("!"))

y = "Welcome to Vrindawan!!!!!!!!!"
print(y)
print("Does the index 4 tp 13 of above atring ends with 'Vr' \n",y.endswith("Vr", 4,13))
print("Does the index 4 tp 13 of above atring ends with 'Vr' \n",y.endswith("Vr", 4,10))
print()

#method find() serches the first occurence of the given value and return the index wwhere it is predent. If given value is absent from the string then rerturn -1.
str1 = "He's name is Dan. He is an engineer."
print(str1)

print("Whereis index of 'is' in above string:\n","At index:",str1.find("is"))

print("Whereis index of 'is' in above string:\n","At index:",str1.find("isss"))
#print("Whereis index of 'is' in above string:\n","At index:",str1.index("isss"))# if string not found then it will throw an error message.
print()

#isalnum()
#this method returns True only if the entire string only consinst of A-Z,a-z,0-9.If any character or puntuation are perdent , then it returns False.
alnum = "WelcomeToTheConsole"
print(alnum)
print(alnum.isalnum())
a="welcome0012"
print(a)
print("Is above string is alphanumric:",a.isalnum())
b = "mOna212@"
print(b)
print("Is above string is alphanumric:",b.isalnum())
#islower

print()
a = "mona"
print(a)
print("Is above string in lowercase:",a.islower())
b = "MONA"
print(b)
print("Is above string in lowercase:",b.islower())
print()

#isprintablale
str = "Wish you a happiest  day Mona"
print(str)
print("Is above string printable:",str.isprintable())
str = "We wish u a happy diwali\n"
print(str)
print("Is above string printable:",str.isprintable())
print()

#isspace
a = "         "#using spacebar key
print(a)
print(a.isspace())

b = "          " #using tab key
print(b)
print(b.isspace())
print()

#istitle()
a = "World Health Organization"
print(a)
print("Is above string title:",a.istitle())

a = "World health organization"
print(a)
print("Is above string title:",a.istitle())
print()

#isupper()


a = "mona"
print(a)
print("Is above string in uppercase:",a.isupper())
b = "MONA"
print(b)
print("Is above string in lowercase:",b.isupper())
print()

#startwith()
a= "Python is an interprator"
print(a)
print("Is above string start with 'Python':", a.startswith("Python"))

a= "Python is an interprator"
print(a)
print("Is above string start with 'Java':", a.startswith("Java"))
print()

#swapcase()
a = "Python is an interprator"
print(a)
print("convert above string's char lowewr to upper and viceversa:\n",a.swapcase())
print()

#title() convert string to title
a = "Python is an interprator"
print(a)
print("convert above string ti title:\n",a.title())
print()


