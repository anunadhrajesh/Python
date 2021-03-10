class Time:
    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        return self.__hour + other.__hour, self.__minute + other.__minute, self.__second + other.__second
print("Time 1")
a=int(input("enter the hour:"))
b= int(input("enter the minute:"))
c= int(input("enter the second:"))
print("Time 1 :-", a, ":", b, ":", c)

print("Time 1")
d=int(input("enter the hour:"))
e= int(input("enter the minute:"))
f= int(input("enter the second:"))
print("Time 2 :-", d, ":", e, ":", f)


t1 = Time(a,b,c)
t2 = Time(d,e,f)
t3 = t1+t2
print("sum of Time 1 and Time 2 =")
print(t3)