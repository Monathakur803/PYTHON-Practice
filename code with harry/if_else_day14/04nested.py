n = int(input("enter the value of num: "))
if n<0:
   print("Number is -ve.")
   
elif n>0:
   if n<=10:
      print("Number is between 1-10.")
      
   elif (n > 10 and n <=20 ):
      print("Number is between 11-20.")
   
   else :
      print("Number is greater than 20")
      
else:
   print("NUmber is zero.")