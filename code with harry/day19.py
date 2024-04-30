print("-------------------------------------------------------------------------------------------------------------------------------")
print("                                                                Day 19                        ")
print("                                                           Break and Continue                ")
print("-------------------------------------------------------------------------------------------------------------------------------")
print()
print("use of Break statement")
for i in range(20):
   print("5 x",i+1,"=", 5*(i+1))
   if i==10:
      break
print("Out of loop now")

print()

print("Continue statement")
for i in range(13):
   if i==10:
      print("Out of loop now")
      break #will leave loop if i=10
   print("5 x",i+1,"=", 5*(i+1))
   
print("Out of loop now")

print()

for i in range(20):
   if i==10:
      print("Skip the iteration")
      continue
   print("5 x",i+1,"=", 5*(i+1))
   
   
   
print()
i=0
while True:
   print(i)
   i=i+1
   
   if i%10 == 0:
      break
      
      