set = {"apple", "banana", "cherry"}
print(set)

#duplicate not allowed
set={"apple","banana","cherry","banana"}
print(set)
print(len(set))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

#add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#for merging two sets
set = {"apple", "banana", "cherry"}
thisset= {"pineapple", "mango", "papaya"}
set.update(thisset)
print(set)
set.remove("banana")
print(set)

#pop
thisset = {"apple", "banana", "cherry"}
x=thisset.pop()
print(x)
print(thisset)

#clear
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


Month=set(["january","february","march","april","may","june","july"])
print(Month)
Month.update(["August","september","october"])
print(Month)

#intersection_update method print the items whic are present in both sets
x = {"apple", "banana", "cherry","google"}
y = {"google", "microsoft", "apple","cherry"}
x.intersection_update(y)
print(x)

#pints the items which are not same in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#return true if no items in set x is present in set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b","a"}
#return true if all items in set x are present in set y
z = x.issubset(y) 
print(z)

#return true if all items set y are present in x
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)


#union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
#set3 = set1.union(set2)
#print(set3)
print(set1|set2)


#intersection
set1 = {"a", "b" , "c",1}
set2 = {1, 2, 3,"a","c"}
print(set1&set2)
print(set1.intersection(set2))




