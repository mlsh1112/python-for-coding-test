def solution(orders, course):
    answer = []
    result=[]
    for i in range(len(orders)):
        for j in range(i+1,len(orders)):
            len_result=len(result)
            for k in orders[j]:
                print(k,orders[j])
                if k in orders[i]:
                    result.append(k)
            if len(result)-len_result<2:
                print(len_result,len(result))
                result.pop()
            answer.append(result)
            print(answer)
    
    return answer

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])