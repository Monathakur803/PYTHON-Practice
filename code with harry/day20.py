print("-------------------------------------------------------------------------------------------------------------------------------")
print("                                                                Day 20                         ")
print("                                                              functions                ")
print("-------------------------------------------------------------------------------------------------------------------------------")
print()

a=8
b=9
geomatric_mean1 =(a*b)/(a+b)
print(geomatric_mean1)
 
c=4
d=9
geomatric_mean2 =(c*d)/(c+d)
print(geomatric_mean2)


#Shorting above code using function
print()

def calcGeoMean(a,b):
   mean = (a*b)/(a+b)
   print(mean)
a=8
b=9
# geomatric_mean1 =(a*b)/(a+b)
# print(geomatric_mean1)
calcGeoMean(a,b)
c=4
d=9
calcGeoMean(c,d)

print()
def calcGeoMean(a,b):
   mean = (a*b)/(a+b)
   print(mean)
print("Geometric mean of 3 and 5:")
calcGeoMean(3,5)
print("Geometric mean of 13 and 5:")
calcGeoMean(13,5)



print()
def calcGeoMean(a,b):
   mean = (a*b)/(a+b)
   print(mean)
a=3
b=5
if a>b:
   print("First number is greater")
else:
   print("Second number is greater")
   
calcGeoMean(a,b)
c=13
d=5
if c>d:
   print("First number is greater")
else:
   print("Second number is greater")
calcGeoMean(c,d)
print()



print()
#using function
def calcGeoMean(a,b):
   mean = (a*b)/(a+b)
   print(mean)
   
def isGreater(a,b):
   if a>b:
      print("First number is greater")
   else: 
      print("Second number is greater")
a=3
b=5
# if a>b:
#    print("First number is greater")
# else:
#    print("Second number is greater")
isGreater(a,b)
calcGeoMean(a,b)

c=13
d=5
# if c>d:
#    print("First number is greater")
# else:
#    print("Second number is greater")
isGreater(c,d)
calcGeoMean(c,d)


print()
#using function
def calcGeoMean(a,b):
   mean = (a*b)/(a+b)
   print(mean)
   
def isGreater(a,b):
   if a>b:
      print("First number is greater")
   else: 
      print("Second number is greater")
      
def isLeser(a,b):
   pass #it means we will use thin  function in future if needed
      
a=3
b=5
isGreater(a,b)
calcGeoMean(a,b)

c=13
d=5
isGreater(c,d)
calcGeoMean(c,d)
print()

'''
Function is of two type 
1) Built-in function: These fun'cn are pre-coded in python ,eg.min(),max(),list(),tuple(),print() etc...
2) User-defined function: These are deefined by user. We can create fun'cn to perforn task as per needed as we have used in above code, like isGreatr etc...
   ''' 





