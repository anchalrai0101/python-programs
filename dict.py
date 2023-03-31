thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(thisdict)
print(thisdict["year"]) #for accessing item

#duplicate values are not allowed
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964,
    "year":2020 #it always gives updated value
}
print(len(thisdict))
print(type(thisdict))

#for find the type of data
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

#dict constructor
thisdict=dict(name="john",age=30,country="norway")
print(thisdict)

#accessing item from other variable
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#x=thisdict["colors"]
x=thisdict.get("brand")
print(x)

#add a new item in original dictionary through key()
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
x=thisdict.keys()
print(x)
thisdict["color"]="white"
print(x)
x=thisdict.values()
print(x)


thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
if "model" in thisdict:
    print("yes,'model'is present in thisdict")

#for removing the item from dict
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
thisdict.pop("model")
#thisdict.popitem()
print(thisdict)

#del keyword also remove the item from dict and delete all elements
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
#del thisdict["year"]
del thisdict
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#loop
dct={"Roll no":101,"Name":"Surbhi","Per":56.8,"Age":21,"ph":987654321,"gender":"Female"}
for i in dct.values():
    print(i)

dct={"Roll no":101,"Name":"Surbhi","Per":56.8,"Age":21,"ph":987654321,"gender":"Female"}
for i ,j in dct.items():
    print(i , j)
#copy
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
mydict = thisdict.copy()
print(mydict)

#Nested
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

x1={}
for i in range(5) :
    k= input("enter key-")
    v= input("enter value-")
    x1[k]=v

print(x1)

k= input("enter key-")
v= input("enter value-")
x1={k:v}
print(x1)

dct={"Roll no":101,"Name":"Deepa","surname":"Kumar","per":78.6,"class":"12th","SchoolName":"SJCS","group":["red","blue","yellow","green","black"]}
print(dct)
print(dct.keys())
print(dct.values())
y= dct.get("per")#get method
print(y)
dct["per"]=85.45
y=dct.items()
print(y)
dct.update({"Name":"Aman"})
print(dct)


#homework
#wap to convert two lists into dictionary
index=[1,2,3]
carname=["breeza","ford","baleno"]
dictionary=dict(zip(index,carname))
print(dictionary)

#wap to merge two dict into one
dict1={1:'a',2:'b',3:'c'}
dict2={4:'d',5:'e',6:'f'}
print(dict1 | dict2)


thisdict={
    "name":"anchal",
    "roll no":12005,
    "phone no":62655865,
    "year":1964,
    "gender":"female"
}
thisdict.pop("phone no")
print(thisdict)

#wap to change the value of year 2004 to 2005

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":2004
}
print(thisdict)
thisdict["year"]=2005
print(thisdict)



