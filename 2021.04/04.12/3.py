import sys
input=sys.stdin.readline

n=int(input())
stack=[]
st_in=[]*n
stack.append(0)
for i in range(n):
  st_in[i]=list(map(str,input()))

for j in range(n):
  no=0
  for i in range(len(st_in[j])):
    if st_in[j][i]=='(':
      stack.append('(')
    elif st_in[j][i]==')':
      if len(stack)==0:
        no=1
        break
      else :
        stack.pop()
  
  if no == 1 :
    print("NO")
  else:
    if len(stack)==1:
      print("YES")
    else:
      print("NO")
       
