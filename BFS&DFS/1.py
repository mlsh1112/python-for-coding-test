def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    if route[x][y]==0:
        route[x][y]=1

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


n,m = map(int, input().split())

route=[list(map(int,input())) for _ in range(n)]


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1


print(result)