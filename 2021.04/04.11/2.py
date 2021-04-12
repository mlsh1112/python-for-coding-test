import sys
input=sys.stdin.readline

n=int(input())

for _ in range(n):
  st=list(map(str,input().split()))
  for i in range(len(st)):
    #object를 string list 로 변경
    st[i]=list(st[i])
    #reversed로 문자열 거꾸로
    reverseSt=reversed(st[i])
    #list를 str로 합치기
    result=''.join(reverseSt)
    print(result)