def solution(numbers, hand):
    answer = ''
    phone=[[3,1],[0,0],[0,1],[0,2], #0,1,2,3
           [1,0],[1,1],[1,2], #4,5,6
           [2,0],[2,1],[2,2], #7,8,9
          ]
    lh=[3,0]
    rh=[3,2]
    for i in numbers:
        if i==1 or i==4 or i==7:
            answer+='L'
            lh=phone[i]
        elif i==3 or i==6 or i==9:
            answer+='R'
            rh=phone[i]
        else:
            now=phone[i]
            llen=abs(now[0]-lh[0])+abs(now[1]-lh[1])
            rlen=abs(now[0]-rh[0])+abs(now[1]-rh[1])
            if llen < rlen :
                answer+='L'
                lh=now
            elif llen > rlen:
                answer+='R'
                rh=now
            else :
                if hand=='right':
                    answer+='R'
                    rh=now
                else:
                    answer+='L'
                    lh=now
            
    return answer