#https://www.acmicpc.net/problem/1158
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
nlist=[0]*n
result=[]
for i in range(n):
  nlist[i]=i+1

num=0
k-=1
result=[]
while nlist:
  num+=k
  while num >= len(nlist):
    num-=len(nlist)
  result.append(str(nlist.pop(num)))

print("<", ", ".join(result)[:], ">", sep='')

