num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)


year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))


num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")


num = int(input("Enter a number: "))  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)  



num = int(input("Enter a number: "))  
factorial = 1  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   for i in range(1,num + 1):  
       factorial = factorial*i  
   print("The factorial of",num,"is",factorial)  



num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)



nterms = int(input("How many terms you want? "))  
n1 = 0  
n2 = 1  
count = 2  
if nterms <= 0:  
   print("Plese enter a positive integer")  
elif nterms == 1:  
   print("Fibonacci sequence:")  
   print(n1)  
else:  
   print("Fibonacci sequence:")  
   print(n1,",",n2,end=', ')  
   while count < nterms:  
       nth = n1 + n2  
       print(nth,end=' , ')  
       # update values  
       n1 = n2  
       n2 = nth  
       count += 1 



def lcm(x, y):  
   if x > y:  
       greater = x  
   else:  
       greater = y  
  while(True):  
       if((greater % x == 0) and (greater % y == 0)):  
           lcm = greater  
           break  
       greater += 1  
   return lcm  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))  



num = int(input("Enter a numer \n"))
count = 0
 
#counting number of digits in 'num'
while num>0:
    count +=1
    num = num//10;
    
print("Number of Digits: %d"%count)



n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)



def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))



n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


























