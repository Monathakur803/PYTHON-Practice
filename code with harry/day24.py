print("-------------------------------------------------------------------------------------------------------------------------------")
print("                                                                Day 23                         ")
print("                                                                Tuples                  ")
print("-------------------------------------------------------------------------------------------------------------------------------")
print()
#tuples are non changable
#tuples, strings are immutable
#lists are mutable
tup=(1,2,3,"Green",2,True)
print(tup,type(tup))
# t=(1,)
# print(t)
print(len(tup))
print(tup[2])
print(tup[1])
print(tup[-3])

if 27 in tup:
   print("Yes")
else:
   print("No")
   
t=tup[1:4]
print(t)