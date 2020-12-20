print("hello world")


a=int(input(enter the integer:"))
print(a)


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
sum = a+b
print("sum :",sum)


num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
mul=num1*num2
print("the product of given numbers is:",mul)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
quotient = a//b
remainder = a%b
print("Quotient is:", quotient)
print("Remainder is:", remainder)


num1 = (input("Enter First Number: "))
num2 = (input("Enter Second Number: "))
print("Value of num1 before swapping: ", num1)
print("Value of num2 before swapping: ", num2)
temp = num1
num1 = num2
num2 = temp
print("Value of num1 after swapping: ", num1)
print("Value of num2 after swapping: ", num2)


num = int(input("Enter a number: "))
if (num % 2) == 0:
print("{0} is Even".format(num))
else:
print("{0} is Odd".format(num))


ch = (input("Enter a character: "))
if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
print(ch, "is a Vowel")
else:
print(ch, "is a Consonant")




