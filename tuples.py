thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Tuples allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Print the number of items in the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

tuple1 = ("abc", 34, True, 40.56, "male")
print(tuple1)

#Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[2])

#Print the last item of the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "kiwi" in thistuple:
    print("yes,'kiwi' is in the fruits tuple")

#change tuple value
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
y=list(thistuple)
print(y)
y[2]="Papaya"
thistuple=tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
y=list(thistuple)
y.append("Papaya")
thistuple=tuple(y)
print(thistuple)

#remove and del,reverse,sort

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
for i in range(len(thistuple)):
    print(thistuple[i])

#while
#join two tuples
tuple1=("a","b","c","d")
tuple2=(1,5,9,4)
tuple3=tuple1+tuple2
print(tuple3)

#Multiply(Repation)
#count
#index()
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
y=thistuple.index("orange")
print(y)





