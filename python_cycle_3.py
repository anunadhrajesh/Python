# -*- coding: utf-8 -*-
"""PYTHON CYCLE 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19s1RssdeVWz3bmVNo-5yvW1aZY283OBQ

1.)
"""

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

"""2.)"""

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

"""3.)"""

total = 0
list1 = [11, 5, 17, 18, 23] 
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("Sum of all elements in given list: ", total)

"""4.)"""

items=[]
for i in range(1000,10000,1):
  for j in  range(32,100,1):
    if i == j*j:
      p=str(i)
      if int(p[0])%2 == 0 and int(p[1])%2 == 0 and int(p[2])%2 == 0 and int(p[3])%2 == 0:
        items.append(p)
print("list of perfect squares from the range 1000 to 10,000 is:",items)

"""5.)"""

row = int(input('Enter how many lines do you want:'))
for i in range(1,row+1):
  for j in range(1, i+1):
    print(i*j, end='')
  print()

"""6.)"""

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('ANUNADH RAJESH'))

"""7.)"""

string = input()
if len(string) < 3:
  print(string)
elif string[-3:] == 'ing':
  print(string + 'ly')
else:
  print(string + 'ing')

"""8.)"""

a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print("The word with the longest length is:")
print(temp)

"""9.)"""

n=int(input("Enter the number:"))
for i in range(n):
  for j in range(i):
    print('*', end="")
  print('')
for i in range(n,0,-1):
  for j in range(i):
    print('*', end="")
  print('')

"""10.)"""

number = int(input("Please Enter any Number: "))

value = 1
print("Factors of a Given Number {0} are:".format(number))

while (value <= number):
    if(number % value == 0):
        print("{0}".format(value))
    value = value + 1

"""11)"""

x=lambda a:a*a
y=lambda b,l:b*1
z=lambda b,h:1/2*b*h
print("Area of Square(5,5):",x(5))
print("Area of Rectangle(20,9):",y(20,9))
print("Area of Triangle(3,4):",z(3,4))

