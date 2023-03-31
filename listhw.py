L=[] 
r=int(input("enter the student roll no:-"))
n=input("enter the student name:-")
m=int(input("how many subject in your course:"))
for i in range(0,m):
  marks=int(input("enter the marks of subject:"))
  L.append(marks)
  print(L)
  print(max(L))

##
p=[]
n=int(input("no of products:"))
for i in range(0,n):
id=int(input("enter the product id:"))
name=input("enter the name of product:")
qty=int(input("enter the quantity of products:"))
up=int(input("enter the unit price:"))
amount=qty*up
p.append(id)
p.append(name)
p.append(qty)
p.append(up)
p.append(amount)
print(p)





