data=list(input())

A=[i for i in data if int(ord(i))>=int(ord('A'))]
B=[i for i in data if int(ord(i))<int(ord('A'))]

A.sort()
B.sort() 
result=0

for i in A:
  print(i,end='')

for i in B:
  result+=int(i)

print(result)