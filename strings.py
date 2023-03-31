s="anchal rai"
print(s)
print(type(s))
s1 =  """example of string""" #we can use three double quotes
print(s1)

str="anchal"
print(str[3])
print(str[0])
#print(str[6]) #out of range

#length
s="hello_world!"
print(len(s))

str1= "welcome"
print(str1[:])  #welcome
print(str1[0:]) #start 0th index to end   #welcome
print(str1[1:5]) #start 1st index to 4th index   #elco
print(str1[2:4]) #start 2st index to 3rd index   #lc
print(str1[:3]) #starat 0th index to 2nd index   #wel
print(str1[4:6]) #starat 4th index to 5th index   #om

print(str1[-1]) #starat 1st index to 4th index     #e
print(str1[-2:]) #starat 1st index to 4th index    #me
print(str1[-6:-2]) #starat 1st index to 4th index   #elco


s1="HELLO"
s2=" WORLD "
print(s1 * 2)  # (*)for multiple time
print(s1+s2)

a = "anchal "
b = "rai"
c = a + b
print(c)


a = "Hello"
b = "World"
c = a + " " + b
print(c)



a = "good morning"
print(a.upper())

a = "GOOD MORNING!!"
print(a.lower())


greet="hello"
for letter in greet:
    print(letter)

a = ",,,,,anchal!!rai,,,......"
p= a.strip(",!.")
print(p)


std = "mca"
txt = "My name is anchal, and I am in {}"
print(txt.format(std))

quantity = "pencil"
itemno = 5
price = 30
myorder = "I want {} pieces of item {} for {} rupees"
print(myorder.format(quantity, itemno, price))



age = 22
name = "shweta"
txt = "Her name is {1}. {1} is {0} years old."
print(txt.format(age, name))


text="hello ,how are you"
x=input("enter any character:")
c=0
for i in text:
    if(i==x):
        c+=1
        print(c)










