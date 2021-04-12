n=10
a=[0]*n

a=[1,2,3,4,5,6,7,8,9]

#뒤 쪽에서 부터 보이려면 인덱스를 음수로
nine=a[-1]
seven=a[-3]
#2,3,4
b=a[1:4]

#[0,1,2,3,4,5,6,7,8,9]
array=[i for i in range(10)]

#홀수만 (리스트 컴프리헨션)
array = [i for i in range(10) if i % 2 ==1]

#4X5
m=5
n=4
array=[[0]* m for _ in range(n)]

a=[1,4,3]
#[1,4,3,2]
a.append(2)
#[1,2,3,4]
a.sort()
#[4,3,2,1]
a.sort(reverse=True)
#[1,2,3,4]
a.reverse()
#인덱스 2에 3을 추가
#[1,2,5,3,4]
a.insert(2,5)
#1
a.count(3)
#[2,5,3,4]
a.remove(1)

# 특정한 값 모두 제거하기
a=[1,2,3,4,5,5,5]
remove_set={3,5}

#[1,2,4]
result=[i for i in a 
        if i not in remove_set]
#"ex
data="\"ex"

#string은 문자 변경 불가

a= "Hello"
b="world"

helloworld=a+b

ell=a[0:4]

#tuple -> 변경 불가능한 객체
a=(1,2,3,4,5,6,7)

# 사전 자료형 -> Key + value
# 변경 불가능한 자료형 -> 키로 사용할 수 있음
#hash table

data=dict()
data['one']=1
data['two']=2

if 'one' in data:
  one=data['one']

key_list=data.keys()
value_list=data.values()

for key in key_list:
  eng=key



d={ 0 : 5 , 1 : 3 , 2 : 4}

items=sorted(d.items(), key=lambda x: x[1])

print(items)

#집합 자료형
#중복 불가
#{1,2,3,4,5}
data=set([1,1,2,3,4,4,5])
#{1,2,3,4,5}
data={1,1,2,3,4,4,5}
data.add(6)
data.update([7,8])
data.remove(3)



n=int(input())
data=list(map(int,input().split()))

#빠른 입력 
import sys

data= sys.stdin.readline().rstrip()

a=10
array[1,2,3]
def func():
  global a
  a=0
  return a

def func2():
  array.append(7)
  return array


