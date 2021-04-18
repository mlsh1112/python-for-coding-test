import sys
slist=list(map(str,input().split('<')))

def soul(slist):
  word=[]
  result=[]
  reverse=[]
  if len(slist)>1:
    for i in slist:
      if not i:
        continue
      result.append('<')
      word=list(i.split('>'))
      result.append(word[0])
      result.append('>')
      if word[1]:
        reverse=[]
        word=list(word[1].split(' '))
        for j in word:
          reverse.append(j[::-1])
        result.append(' '.join(reverse))
      
  else:
    slist=list(slist[0].split(' '))
    for i in slist:
      result.append(i[::-1])
      result.append(' ')
    result.pop()
  return(''.join(result))

print(soul(slist))