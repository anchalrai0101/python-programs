ls=["ram",50,18.25,"true",80,0.25,"deepak","kirti",154,32.58]
print(ls)
#print(type(ls))
print(len(ls))
print(ls[2])
print(ls[-2])

#slicing
print(ls[:])
print(ls[1:4])
print(ls[-1:-4])
print(ls[:4])
print(ls[3:])
print(ls[-6:-2])

list=[1,2,3,4,5,6]
print(list)
list[2]=5
print(list)
list[1:4]=[84,36]
print(list)
list[-1]=12
print(list)

thislist=["apple","banana","papaya","guava"]
if "orange" in thislist:
  print("Yes, 'orange' is in the fruits list")
else:
  print("No, it's not.")
l1= [5,8,3,9,7]  
l1.reverse()
print(l1) 

#insertitem
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "papaya")
print(thislist)

#append 
thislist = ["apple", "banana", "cherry","carrot","grapes"]
thislist.append("orange")
print(thislist)

#extend
ls= ["apple", "banana", "cherry"]
l1= ["mango", "orange","watermelon", "papaya"]
ls.extend(l1)
print(ls)

#remove
thislist = ["apple", "banana", "cherry","tomato"]
thislist.remove("tomato")
print(thislist)

#pop()
thislist = ["apple", "banana", "cherry","grapes","watermelon"]
thislist.pop(4)
print(thislist)

#del
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)

#clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#loop index no
thislist = ["apple", "orange", "banana","mango", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#short list
thislist = ["orange", "Mango", "kiwi", "Pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Reverse order
thislist = ["bv", "TT", "ss", "Ram"]
thislist.reverse()
print(thislist)

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join Two List
list1 = ["a", "b", "c"]
list2 = ["l", "m", "n"]

list3 = list1 + list2
print(list3)

#Repetition
ls=["Ram","sita","gita"]
print(ls*2)

#Adding element to the list
L=[] #declaring Empty list
n= int(input("enter the number of element in the list:-"))
for i in range(0,n):
  L.append(input("enter the item-"))
print("Printing list item-")
for i in L:
  print(i,end=",") 

#Max value
thislist = [1, 5, 6, 2, 3]

print(max(thislist))

list1=["i","anc","ra",]
list2=["am","hal","i"]
list3=[i+j for i,j in zip(list1,list2)]
print(list3)



 


