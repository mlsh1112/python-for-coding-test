#https://www.acmicpc.net/problem/10845

import sys
input=sys.stdin.readline

n=int(sys.stdin.readline())
queue=[]
for _ in range(n):
  tmp=sys.stdin.readline().split()
  
  if tmp[0]=='push':
    queue.append(tmp[1])

  elif tmp[0]=='front':
    if not queue:
      print(-1)
    else:
      print(queue[0])

  elif tmp[0]=='pop':
    if not queue:
      print(-1) 
    else:
      print(queue.pop(0))
      
  elif tmp[0]=='back':
    if not queue:
      print(-1)
    else:
      print(queue[-1])
      
  elif tmp[0]=='empty':
    if not queue:
      print(1)
    else:
      print(0)

  elif tmp[0]=='size':
    print(len(queue))
