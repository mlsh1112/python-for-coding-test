N,M = map(int, input().split())
route=[]
result=0
for i in range(N):
  route.append(list(map(int,input())))


def dfs(x,y):
  global result
 
  if x<0 or x>=N or y<0 or y>=M:
    return



  if route[x][y]==1:
    print(x,y)
    result+=1
    route[x][y]=0
  else:
    return

  dfs(x+1,y)
  dfs(x,y+1)
  dfs(x-1,y)



dfs(0,0)
print(result-1)