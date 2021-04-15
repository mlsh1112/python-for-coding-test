#https://www.acmicpc.net/problem/1158
import sys
input=sys.stdin.readline

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



