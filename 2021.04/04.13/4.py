#https://www.acmicpc.net/problem/1874
n=int(input())
result=[]
stack=[]
max_data=0
stack.append(0)
for _ in range(n):
  data=int(input())
  if stack[-1]>data:
    break
  elif stack[-1]==data:
    stack.pop()
    result.append('-')

  else:
    for i in range(max_data,data):
      stack.append(i+1)
      result.append('+')
    data=stack.pop()
    if data > max_data:
      max_data=data
    result.append('-')


if stack[-1]!=0:
  print('NO')
else :
  for i in result:
    print(i)
