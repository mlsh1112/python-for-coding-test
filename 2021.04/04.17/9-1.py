
import sys
input=sys.stdin.readline

sinput=list(input())
tag=False
word=''
result=''

for i in sinput:
  if tag==False:
    if i=='<':
      tag=True
      word=word+i
    elif i==' ':
      word=word+i
      result=result+word
      word=''
    else:
      word=i+word

  elif tag==True:
    word=word+i
    if i=='>':
      tag=False
      result=result+word
      word=''

print(result+word)