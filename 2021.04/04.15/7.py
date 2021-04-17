#https://www.acmicpc.net/problem/1158
import sys
input=sys.stdin.readline

<<<<<<< HEAD
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
=======
n=int(input())
k=int(input())
nlist=[]

for i in range(n):
  nlist[i]=i+1

num=-1+k
result=[]
while nlist:
  pre=num
  num+=k
  if num > len:
    num=num-len(nlist)-1



>>>>>>> 36dbe5d2a1cd4979b24ca733d0729b559e117e09
