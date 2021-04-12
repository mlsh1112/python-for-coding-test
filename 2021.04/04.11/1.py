def __init__ (self):
  self.top=[]

def __len__(self):
  return len(self.top)

def __str__(self):
  return str(self.top[::1])

def push(self,item):
  self.top.append(item)

def pop(self):
  if not self.isEmpty():
    return self.top.pop(-1)
  else:
    return -1

def top(self):
  if not self.isEmpty():
    return self.top(-1)
  else:
    return -1

import sys

input=sys.stdin.readline
n=int(input())
stack=[]
for _ in range(n):
  l=list(input().split())
  if l[0] == 'push':
    stack.append(int(l[1]))
  elif l[0]=='pop':
    if len(stack)==0:
      print(-1)
    else:
      print(stack.pop())
  elif l[0]=='top':
    if len(stack)==0:
      print(-1)
    else:
      print(stack[-1])
  elif l[0]=='size':
    print(len(stack))
  elif l[0]=='empty':
    if len(stack)==0:
      print(1)
    else:
      print(0)
  

