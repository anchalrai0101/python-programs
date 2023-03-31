num=int(input("enter any number"))
if num%2==0:
    print("it is even number")


age=int(input("enter your age"))
if age>=18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")


age=int(input("enter your age"))
if age>=21:
    print("your age is valid for marriage")
else:
    print("your age is not valid for marriage")


#1.max btw two numbers
num1=int(input("enter the first no:"))
num2=int(input("enter second no:"))
if num1>num2:
    print(num1,"is greater")
else:
    print(num2," is greater")


#2.find a max no between three numbers
num1=int(input("enter the first no:"))
num2=int(input("enter second no:"))
num3=int(input("enter third no:"))
if num1>num2 and num1>num3:
    max=num1
elif num2>num1 and num2>num3:
    max=num2
else:
    max=num3

print(max,"is the maximum of three numbers")

#3.whether a number is negative, positive or zero.
num=int(input("enter the number:"))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("equal to zero")

#4.check whether the no is divisible by 5 & 11 or not
num=int(input("enter any number"))
if num%5==0 and num%11==0:
    print("number is divisible by 5 & 11")
else:
    print("number is not divisible by 5 & 11")


#5.check whether the number is even or odd
num=int(input("enter any number:"))
if num%2==0:
    print(num,"is even number")
else:
    print(num,"is odd number")


#6.whether the year is leap year or not
year=int(input("enter the year:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(year,"is a leap year")
        else:
            print(year,"is not leap year")
    else:
        print(year,"is leap year")
else:
    print(year,"is not leap year")


#7.check whether the char is alphabet or not
char=int(input("enter any character:"))
if (char>='A' and char<='Z'):
    print(char,"is alphabet")
elif(char>='a'and char<='z'):
    print(char,"is alphabet")
       
else:
    print(char,"is not alphabet")

#8.check whether the enter alphabet is vowel or consonant
ch = input("Enter a character: ")
if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")


#9.enter char is alphabet 
char=input("enter any character:")
if(char>='a'and char<='z'):
    print(char,"is alphabet")
elif(char>='0'and char<='9'):
    print(char,"is a digit")
else:
    print(char,"is a special symbol")


#10.enter char is uppercase or lowercase
char=input("enter any character:")
if(char>='A' and char<='Z'):
    print(char,"is uppercase letter")
elif(char>='a'and char<='z'):
    print(char,"is lower case letter")
else:
    print(char,"is  not lowercase letter or not uppercaseletter")

#11.print week no and week days
num=int(input("enter any week day num(1-7):"))
if(num==1):
    print("sunday")
elif(num==2):
    print("monday")
elif(num==3):
    print("tuesday")
elif(num==4):
    print("wednesday")
elif(num==5):
    print("thuresday")
elif(num==6):
    print("friday")
elif(num==7):
    print("saturday")
else:
    print("this number is not a week day number")


#12.find profit or loss
sp=float(input("enter the selling price:"))
cp=float(input("enter the cost price:"))
if(sp>cp):
    profit=sp-cp
    print("profit=",profit)
elif(sp<cp):
    loss=cp-sp
    print("loss=",loss)
else:
    print("no profit no loss")
    

               

