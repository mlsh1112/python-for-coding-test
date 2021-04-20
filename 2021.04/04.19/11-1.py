n=int(input())
num=list(map(int,input().split()))
stack=[]

result=[-1 for _ in range(n)]

for i in range(len(num)):
<<<<<<< HEAD
  while len(stack)!=0 and num(stack[-1])<num[i]:
=======
  while len(stack) and num(stack[-1])<num[i]:
>>>>>>> c5e9352672886031de8b1117b8cab9b2b00954d1
    result[stack.pop()]=num[i]
  stack.append(i)

print(*result)