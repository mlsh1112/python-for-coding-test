#https://www.acmicpc.net/problem/10866
import sys
input=sys.stdin.readline

defront=[]
deback=[]
n=int(input())
result=[]
for _ in range(n):
  temp=list(input().split())
  if temp[0]=='push_front':
    defront.append(temp[1])
    deback=defront+deback
    defront=[]
  elif temp[0]=='push_back':
    deback.append(temp[1])
  elif temp[0]=='pop_front':
    if not deback:
      result.append(-1)
    else:
      result.append(deback.pop(0))
  elif temp[0]=='pop_back':
    if not deback:
      result.append(-1)
    else:
      result.append(deback.pop(-1))
  elif temp[0]=='size':
    result.append(len(deback))
  elif temp[0]=='empty':
    if not deback:
      result.append(1)
    else:
      result.append(0)
  elif temp[0]=='front':
    if not deback:
      result.append(-1)
    else:
      result.append(deback[0])
  elif temp[0]=='back':
    if not deback:
      result.append(-1)
    else:
      result.append(deback[-1])

for i in result:
  print(i)


  