x,y=(input())
y=int(y)
al_x=['a','b','c','d','e','f','g','h']

for i in range(8):
  if x==al_x[i]:
    x=i+1

count=0
d1=[-1,1]
d2=[-2,2]

for i in range(2):
  for j in range(2):
    n_x=x+d1[i]
    n_y=y+d2[j]
    if n_x<1 or n_y<1 or n_x>8 or n_y>8:
      continue
    count+=1

for i in range(2):
  for j in range(2):
    n_x=x+d2[i]
    n_y=y+d1[j]
    if n_x<1 or n_y<1 or n_x>8 or n_y>8:
      continue
    count+=1



print(count)