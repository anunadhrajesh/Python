f=open("py.txt","r")
content=f.readlines()
print("file content is",content)
x=['qwerty']
x.append(content)
print("after append line is",x)
