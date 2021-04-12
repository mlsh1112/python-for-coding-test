import sys
input=sys.stdin.readline

n=int(input())
stack=[]
stack.append('0')
for _ in range(n):
  ps=list(map(str,input()))
  for i in range(len(ps)):
    if ps[i]=='(':
      stack.append('(')
    else:
      if len(stack)==0:
        stack.append('0')
        break
      else:
        stack.pop()
  
  if len(stack)==0:
    print('YES')
  else:
    print('NO')
