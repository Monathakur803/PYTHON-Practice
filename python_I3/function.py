'''
def output(a,b=30): # here a, b are paremater
   print("Hello",a+b)
   
output(10,20) #here 10,20 are argument
'''

'''
def output(a,b): # here a, b are paremater
   return a+b
   print("Hello")
   
ans = output(10,20) #here 10,20 are argument
print(ans)
'''

#-----------------lambda function----------

'''
a=[10,20,30]
x = lambda a:a**2
print(x(10))
'''

#-------------------High order function--------
'''
l= [10,20,30,40,50]
x =list(map(lambda x:x**2,l))
print(x)'''


 
'''
l= [10,20,30,40,50]
x= list(map(lambda x:x**2,l))

y = list(filter(lambda x:x>=30,l))
print(y)
'''
'''
d = [
   {
      "id":1,
      "name":"Mona",
      "Age": 20,
      "city": "Jaipur"
   },
   {
      "id":2,
      "name":"Aman",
      "Age": 25,
      "city": "Jodhpur"
   },
   {
      "id":3,
      "name":"Rohit",
      "Age": 15,
      "city": "Udaipur"
   },
   {
      "id":4,
      "name":"Anu",
      "Age": 5,
      "city": "Kota"
   }
   
]
x= list(map(lambda x:x,d))
print(x)
print("\n")
y = list(filter(lambda x:x["Age"]>= 18,d))
print(y)
'''



d = [
   {
      "id":1,
      "name":"Mona",
      "Age": 20,
      "city": "Jaipur",
      "p":55,
      "c":40,
      "m":75
   },
   {
      "id":2,
      "name":"Aman",
      "Age": 25,
      "city": "Jodhpur",
      "p":52,
      "c":80,
      "m":55
   },
   {
      "id":3,
      "name":"Rohit",
      "Age": 15,
      "city": "Udaipur",
      "p":95,
      "c":70,
      "m":5
      
   },
   {
      "id":4,
      "name":"Anu",
      "Age": 5,
      "city": "Kota",
      
      "p":25,
      "c":40,
      "m":65
   }
   
]
# x= list(map(lambda x:x,d))
# print(x)
# print("\n")
# y = list(filter(lambda x:(x["p"]+x["c"]+x["m"])/300,d))
# print(y)


x= list(filter(lambda x:((x["p"]+x["c"]+x["m"])/3)>50,d))
 
for i in x:
   print(i)

print("\n")
 