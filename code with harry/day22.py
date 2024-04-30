print("-------------------------------------------------------------------------------------------------------------------------------")
print("                                                                Day 22                         ")
print("                                                             Intro to List                  ")
print("-------------------------------------------------------------------------------------------------------------------------------")
print()


marks = [1,2,5,4,'Mona',True] #we can add two diff type of data in list
print(marks,type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[4])
print("length",len(marks))
print()
print("slicing")
print(marks[1:5:2])
print(marks[1:])
print(marks[2:5])
print(marks[-1:1])
print(marks[-2:-4])
if 5 in marks:
   print("Yes")
else:
   print("No")
   
if "Mo" in "Mona":
   print("Yes")
else:
   print("No")
print()

print("List comprehenson:")

lst = [i for i in range(4)]
print(lst)

lst = [i*2 for i in range(8)]
print(lst)

lst = [i*i for i in range(9)  if i%2==0]
print(lst)
# Add more data in list:
#we can add two diff type of data in list

print("Accepts item which have more than 4 letters")

names =["Mona","Jayash","Pooja","Sai","Pushpa"]
x = [i for i in names if (len(i)>4)]
print(x)
