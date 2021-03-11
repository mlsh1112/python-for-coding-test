#상하좌우
n = int(input())
array = [[0 for _ in range(n)]for row in range(n)]

x,y=0,0

route = list(input().split())

for i in route:
  if i=='L':
    if y==0:
      continue
    y-=1
  elif i=='R':
    if y==(n-1):
      continue
    y+=1
  elif i=='U':
    if x==0:
      continue
    x-=1
  else:
    if x==(n-1):
      continue
    x+=1

print(x+1,y+1)