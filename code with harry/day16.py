print("--------------------------------------------------------------------day16------------------------------------------------------------")
print("----------------------------------------------------------Match Case Statements------------------------------------------------")

x = int(input("Enter your age: "))

match x:
   case 0:
      print("x i zero")
   case 4:
      print("Case is 4")
      
   case _ if x!=90:
      print(x,"is not 90")
      
   case _ if x!=80:
      print(x,"is not 80")