import sys
input=sys.stdin.readline

line=list(input())
cut=False
result=0
#각 쇠 막대기마다 몇 번 잘리는 지 쇠막대기의 잘리는 횟수를 stack에 저장
stack=[]

for i in line:
  if i == '(':
    cut=True
    stack.append(i)
    #새로운 막대가 추가될때 result에 막대 하나 추가
    result+=1
  elif i == ')':
    stack.pop()
    #쇠 막대기가 아니라 레이져일 때
    if cut==True:
      #레이져이므로 result에서 막대 개수를 빼준다
      result-=1
      #레이져로 자를때 막대기가 있는 만큼 생기므로 result에 더해준다
      result+=len(stack)
    cut=False

  
print(result)

