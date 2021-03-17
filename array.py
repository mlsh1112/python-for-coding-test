n,m=map(int, input().split())

mylist=[0 for _ in range(n)]
for i in range(n):
    mylist[i]=list(map(int,input().split()))


mylist=[]
for i in range(n):
    mylist.append(list(map(int,input().split())))

mylist=[list(map(int,input().split())) for _ in range(n)]