print("-------------------------------------------------------------------------------------------------------------------------------")
print("                                                                Day 23                         ")
print("                                                           Methods of List                  ")
print("-------------------------------------------------------------------------------------------------------------------------------")
print()

l = [1,2,4,3]
print(l)
l.append(10)
print("After appending 10 to above list:",l)
l.reverse()
print("After reversing above list:",l)
li=[2,1,4,5,6,7]
li.sort(reverse=True)
print("After sorting above list:",li)
li=[2,1,4,5,6,7]
print(li)
print("Index of 4 is:",li.index(4))
l=[2,1,1,2,3,4,2,2]
print(l)
print("No of occurence of 2:",l.count(2))
print()

m=l
m[0]=0
print(l)

m=l.copy()
m[0]=0
print(l)
print()
l=[11,23,2,4,5,6,4,1,1]
print(l)
l.insert(2,20)
print(l)

m=[900,110,1100]
l.extend(m)
print("Extende above list with new list:",l)

k= l+m
print(k)

