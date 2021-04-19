#https://www.acmicpc.net/problem/17298
import sys
input=sys.stdin.readline
N=int(input())
data=list(map(int, input().split()))
result=[-1]*N
ren=data.pop()
for i in range(1,N):
  nown=data.pop()
  if nown < ren :
    result[i]=ren
  else:
    if result[i-1]>nown:
      result[i]=result[i-1]
  ren=nown
    
print(*result[::-1])