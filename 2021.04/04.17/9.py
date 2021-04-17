slist=list(map(str,input().split()))
word=[]
result=[]
reverse=0

for i in slist:
  word=list(i)
  



  word.reverse()
  if i == '<':
    reverse=1
    word.append(i)

    continue
  elif i == '>':
    reverse=0
    word.append(i)
    result=result+word
    word=[]
    continue
  
  elif i == ' ':
    word.pop()
    if not reverse:
      word.reverse()
    result+=word
    word=[]
    continue


  print(word)
  
  
  

print(result)
  
  
