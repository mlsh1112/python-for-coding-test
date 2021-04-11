#프로그래머스 네트워크
def solution(n, computers):
    answer = 0
    visited=[False]*n
    
    def dfs(num):
        if visited[num]==False:
            visited[num]=True
            for i in range(n):
                if i != num and computers[num][i]:
                    dfs(i)
    
    for i in range(n):
        if visited[i]==False:
            answer+=1
            dfs(i)
    
    return answer