print("------Armstrong number-----")
n = int(input("Enter the number to check wether the number is armstrong or not \n"))
sum = 0
order = len(str(n))
y = n
while(n>0):
   x = n%10
   sum += x **order
   n= n//10
   
if(sum == y):
   print(f"{y} is armstrong number")
else:
   print(f"{y} is not an armstrong number")

