import calendar
class Atm():
   
   def  __init__(self):
     self.bank = 0
     self.pin = ''
     self.menu()
   
   def menu(self):
      
       print('''
         press 1 for generate new pin
         press 2 for deposite amount
         press 3 for withdraw amount
         press 4 for checking balance 
         press 5 to exit
         press 6 to check history
         ''')
     
       x = int(input("Enter : "))
   
       if x == 1:
         self.genrate_pin()
      
       elif x == 2:
        self.deposite_amt()
      
       elif x == 3:
          self.withdraw_amt() 
          
       elif x == 4:
          self.check_amt()
          
       elif x == 5:
          self.exit()
          
       elif x == 6:
          self.hist()
          
       else:
          print("Please enter correct option 1/2/3/4/5/6")
          self.menu()
          
          
      
      
   def genrate_pin(self):
      self.pin = input("enter your new pin ")
      print("Pin sucessfully set!!\n")
      self.menu()
      
   def deposite_amt(self):
      your_pin = input("Enter your pin ")
      if(self.pin == your_pin):
         your_amt = int(input("Enter your amount "))
         self.bank+= your_amt
         print("sucessfully deposited")
      else:
         print("Incorrect")
         
      self.menu()
      
   def withdraw_amt(self):
      your_pin = input("Enter your pin ")
      if(self.pin == your_pin):
         et_amt = int(input("Enter your amount "))
         if et_amt > self.bank:
            print("You do not have sufficient balance :( \n")
            
         else:
           self.bank = self.bank - et_amt
           print("You have withdrawn",et_amt)
           x= self.bank
           print("Your current balance is : " , x)
        # if et_amt > self.bank:
         #   print("You do not have sufficient balance :( \n")
            # self.bank = self.bank - et_amt
            # print("You have withdrawn",et_amt)
            # x= self.bank
            # print("Your current balance is : " , x)
      else:  
         print("Incorrect")
         
      self.menu()
      
      
   def check_amt(self):
      your_pin = input("Enter your pin ")
      if(self.pin == your_pin):
         x = self.bank
         print("your balance is : ", x)
      else:
         print("Incorrect")
         
      self.menu()
      
      
   def exit(self):
       print(" Thik hai by by.. ")
       
   def hist(self):
      self.hist = 12
   
      
          
   
   
obj1 =Atm()
 
