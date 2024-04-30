print("---------------------------------------------------------------------")
print("                                 Day 26                     ")
print("                               Exercise 2    ")
print("---------------------------------------------------------------------")
print()
'''
  
'''




 #Exercise 2 to greet with good Morning, goof afternoon and good evening!!

import time
t = time.strftime('%H:%M:%S')
print(t)
t = int(time.strftime('%H'))

if t<=12:
   print("Good morning!!")
   
elif 12<=t<=18:
   print("Good afternoon!!")
   
else:
   print("Good evening!!")