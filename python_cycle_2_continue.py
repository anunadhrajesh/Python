# -*- coding: utf-8 -*-
"""PYTHON CYCLE 2 CONTINUE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T8BNWF4QsdcX24jW-cuTXTyFVUnzfMzP

1.)
"""

n=input("enter your house number : ")
hname=input("enter your house name : ")
s=input("enter your street name : ")
t=input("enter your town/city : ")
d=input("enter your district : ")
state=input("enter your state : ")
county=input("enter your county : ")
pin=int(input("enter your postcode: "))
print("\nAddress Details :\n" + "\nHousenumber :",n,"\nHouse :",hname,"\nStreet : ",s,"\nTown/City : ",t,"District : ",d,"\nState : ",state,"\nCounty : ",county,"\nPostcode : ",pin)

"""7.)"""

78
x=[]
a=int(input("enter limit for list1 : "))
for i in range(1,a+1):
  a=int(input())
  x.append(a)
print(x)
y=[]
b=int(input("enter limit for list2 : "))
for i in range(1,b+1):
  b=int(input())
  y.append(b)
print(y)
if (len(x)==len(y)):
  print("list1 and list2 are of same length i.e.",len(x))
else:
  print("list1 and list2 are of different length.")
if (sum(x)==sum(y)):
  print("list1 and list2 sums to the same value i.e.",sum(x))
else:
  print("list1 and list2 sums up to different values.")
def common(x, y): 
    p=set(x) 
    q=set(y) 
    if len(p.intersection(q)) > 0: 
        return(p.intersection(q))   
    else: 
        return("no common elements")  
print("value that occur in both lists is/are :",common(x,y))

"""8.)"""

str=input("enter any string : ")
def rep_ch(str1):
  char=str1[0]
  str1=str1.replace(char, '$')
  str1=char+str1[1:]
  return str1
print(rep_ch(str))

color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))

def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))

import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)

def Merge(dict1, dict2):
    return(dict2.update(dict1))
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(Merge(dict1, dict2))
print(dict2)

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
i = 1
while(i <= num1 and i <= num2):
  if(num1 % i == 0 and num2 % i == 0):
    gcd = i
  i = i + 1
print("GCD is", gcd)

num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)