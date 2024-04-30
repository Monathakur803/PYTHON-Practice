print("--------------------------------------------------------------------day11------------------------------------------------------------")
print("---------------------------------------------------------------String in python-----------------------------------------------------")

name = "Mona"
frnd = "Pooja"
anotherfrnd =  "Yash"

apple  = '''Use the random module.: The random module can be used to generate random text, 
including Lorem Ipsum text. To generate Lorem Ipsum text using the random module, you would
need to create a list of words and then randomly select words from the list to create a sentence or paragraph. '''

print("Hello," + name)

print(apple)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
#print(name[5]) #will give error  IndexError: string index out of range
print(apple[4])
print(frnd[3])
print(apple[8])
print(anotherfrnd[3])
print(frnd[0])

print("Lets print each index character using for loop")

for i in apple:
   print(i, end= ", ")
print()

for j in name:
   print(j)