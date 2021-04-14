#https://www.acmicpc.net/problem/1406
#시간 초과
import sys
import time
input=sys.stdin.readline()
stlist=list(map(str,input()))
n=int(input())
top=len(stlist)
for _ in range(n):
  go=list(map(str,input().split()))
  if go[0]=='L':
    if top==0:
      continue
    else:
      top-=1
  elif go[0]=='D':
    if top==len(stlist):
      continue
    else:
      top+=1

  elif go[0]=='B':
    if top==0:
      continue
    else:
      top-=1
      stlist.pop(top)

  elif go[0]=='P' :
    stlist.insert(top,go[1])
    top+=1

for i in stlist:
  print(i,end='')