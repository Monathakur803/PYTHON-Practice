print("Welcome to my computer quiz  !!")
playing = input("Do you want to play ??")

if playing  != "yes":
   quit()
   
print("Okay let's play :)")
score = 0

answer = input(" What does CPU stands for?  ")
if answer.lower() == "Centeral Processing unit":
   print('Correct!') 
   score += 1 
else:
   print("Incorrect!")
   

answer = input("  What does GPU stands for?  ")
if answer == "Graphic Process unit":
   print('Correct!') 
   score += 1 
else:
   print("Incorrect!")


answer  = input("  What does RAM stands for? ")
if answer  == "RAndom Accesss Memory":
   print('Correct!') 
   score += 1 
else:
   print("Incorrect!")


answer  = input("National bird of India ")
if answer  == "Pecock":
   print('Correct!') 
   score += 1
else:
   print("Incorrect!")


answer = input("King of animal ")
if answer  == "Lion ":
   print('Correct!')  
   score += 1
else:
   print("Incorrect!")


answer = input("What is full form of ROM? ")
if answer  == "Read Only Memory":
   print('Correct!')  
   score += 1
else:
   print("Incorrect!")
   
print("You got " + str(score) + " Questions correct!")
print("You got " + str((score / 4) * 100) + "%")

