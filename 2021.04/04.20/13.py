def solution(s):
    answer = []
    #{} 문자열 제거
    slist=s.lstrip('{').rstrip('}').split('},{')
    # 문자 길이 순서로 정렬
    slist.sort(key=lambda x:len(x))
    
    for i in range(len(slist)):
        tu=slist[i].split(',')
        for j in tu:
            j=int(j)
            #집합에 있는 수가 answer에 있는지 확인 후 push
            if not j in answer:
                answer.append(j)
    
    return answer