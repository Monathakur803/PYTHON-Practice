num = int(input("enter number:"))
sum = 0
y = num
count = len(str(num))
while(num>0):
   x = num%10
   sum += x**count
   num =num//10
if (sum == num):
   print("is armstrong")
else:
   print("not an armstrong")