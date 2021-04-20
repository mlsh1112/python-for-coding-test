n=int(input())
num=list(map(int,input().split()))
stack=[]

result=[-1 for _ in range(n)]

for i in range(len(num)):
  while len(stack)!=0 and num(stack[-1])<num[i]:
    result[stack.pop()]=num[i]
  stack.append(i)

print(*result)