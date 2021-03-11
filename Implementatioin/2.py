n= int(input())
count=0

while(n+1):
  for hour in range(60):
    for second in range(60):
      if(hour//10==3 or hour%10==3 or second//10==3 or second%10==3 or n%10==3 or n//10==3):
        count+=1
  n-=1


print(count)