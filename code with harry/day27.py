print("--------------------------------------------------------------------")
print("                                  day 27  ")
print("                      Exercise 3: Kaun Banega Crorpati      ")
print("--------------------------------------------------------------------")
print()

'''
Create a program capable of displaying queston to the user like KBC.
Use List data type to store the question and there correct answers.
Display the final amount the person is taking home after playing the game.

'''
def lst():
   for i in op:
     print(i)
     
print("\nQ1:")
price =0
l=["Who is PM of Bharat?"]
print(l)

op = ["a: Narindar Modi",
      "b: Jawaharlal Nehru",
      "c: Arwind Kejriwal",
      "d: Lalu Yadav"]
lst()
   
#print(op)
print("select yor option:\n")
ans = input()
if "a" in ans:
   print("Correct✅")
   price=10000
   print("Congrats You won 10000$")
else:
   print("wrong❌")
   if price>500:
      price=price-500
      print("Sorry you loose 5000$ ")
   
   
print("\nQ2:")
q2=["Who is CM of Bihar?"]
print(q2)
op = ["a: Lalu Yadav",
      "b: Jawaharlal Nehru",
      "c: Nitish kumar",
      "d: Lalu Yadav"]
lst()
ans = input()
if "c" in ans:
   print("Correct✅")
   price=price+10000
   print("Congrats You won 10000$")
else:
   print("wrong❌")
   if price>500:
      price=price-500
    
      print("Sorry you loose 500$ ")
   
   
print("\nQ3: ")
q3=["Whate is the color of Danger sign?"]
print(q3)
op = ["a: Lal ",
      "b: Blue",
      "c: Black",
      "d: Green"]
lst() 
ans = input()
if "a" in ans:
   print("Correct✅")
   price=price+10000
   print("Congrats You won 10000$")
else:
   print("wrong❌")
   if price>500:
      price=price-500
      print("you loose 500$")


print("\nQ4: ")
q4=["How many continent are there?"]
print(q4)
op = ["a: 3 ",
      "b: 10",
      "c: 4",
      "d: 7"]
lst() 
ans = input()
if "d" in ans:
   print("Correct✅")
   price=price+10000
   print("Congrats You awarded 10000$")
else:
   print("wrong❌")
   if price>500:
      price=price-500
      print("Sorry you loose 500$ ")
   
print("\nQ5: ")
q5=["National animal"]
print(q5)
op = ["a: Elephent ",
      "b: Tiger",
      "c:  Lion",
      "d: Goat"]
lst() 
ans = input()
if "c" in ans:
   print("Correct✅")
   price=price+10000
   print("Congrats You awarded  10000$")
else:
   print("wrong❌")
   if price>500:
      price=price-500
      print("Sorry you loose 500$ ")
if price>1:
   print("\nCongratulations🎉 you win",price,"$ price money!!\n")
else:
   print("Better luck next time!!")