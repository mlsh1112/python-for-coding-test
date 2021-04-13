n=int(input())
def soul(st_in):
  stack=[]
  for i in st_in:
    if i=='(':
      stack.append(i)
    elif i==')':
      if not stack:
        print('NO')
        return
      else :
        stack.pop()
  if not stack:
    print('YES')
  else :
    print('NO')
  return

for _ in range(n):
  st_in=input()
  soul(st_in)
