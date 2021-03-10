#모험가 길드 문제

n=int(input())
data=list(map(int,input().split()))
result=0

data.sort()
num=0

while True:
  num+=data[num]
  if num>n:
    break
  elif num==n:
    result+=1
    break
  result+=1


print(result)