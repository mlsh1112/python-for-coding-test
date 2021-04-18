import sys
input=sys.stdin.readline

stk1=list(map(str,input().strip()))
stk2=[]
n=int(input())
for _ in range(n):
  go=list(map(str,input().split()))
  
  if go[0]=='L' and stk1!=[]:
    stk2.append(stk1.pop())
  elif go[0]=='D' and stk2 !=[]:
    stk1.append(stk2.pop())
  elif go[0]=='B' and stk1!=[]:
    stk1.pop()
  elif go[0]=='P':
    stk1.append(go[1])

print("".join(stk1+list(reversed(stk2))))
