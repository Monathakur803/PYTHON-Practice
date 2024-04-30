print("---------------------------------------------------------------------")
print("                                 Day 23                     ")
print("                           Operations on Tuples             ")
print("---------------------------------------------------------------------")
print()
'''
   MANIPULATING TUPLES:
   
  Tuples are immutable, hence if we want to ad or remove or change , 
  then first you must convert the tuple to list. Then perform operation
  on that list and convert it back to tuples.
'''

countries = ("Spain",'India','italy','England','germany')
print(countries)
print()
temp = list(countries)
print("Converted above tuple into list:\n",temp)
print()
temp.append("Russia")
print("Appended Russia:\n",temp)
print()
temp.pop(3)
print("Remove England:\n",temp)
print()
temp[2]="Finland"
print("Add Finlan on 2nd index:\n",temp)
print()
countries = tuple(temp)
print("Finally again converted back into tuple:\n",countries)
print()

print("Meerging two tuple without converting into list")

countries = ("Spain",'India','italy','England','germany')
print("Tuple1:\n",countries)
countries2 = ("Newyork",'Switzerland','Shrilanka','Bangladesh','China')
print("Tuple2:\n",countries2)
south_asia = countries+countries2
print("After merging above two tuples:\n",south_asia)
print()
a = (1,2,1,3,4,3,2,1,2,3,4,3,2,1,1)
print(a)
x =a.count(1)
print("Number of occurence of 1:",x)

a = (1,2,1,3,4,3,2,1,2,3,4,3,2,1,1)
b =a.index(4)
print("what is indexof 4:",b)

b = a.index(3,4,8)
print("\n",b)

print("\n","length:",len(a))
