#카카오 2019 인턴 크레인 인형뽑기
#https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    #크레인으로 뽑은 인형을 담는 배열
    stack=[]
    stack.append(0)
    for num in moves:
        #doll은 뽑아진 인형의 번호이다
        doll=0
        #moves가 가리킨 배열의 가장 위의 인형을 doll에 입력한다
        for i in range(len(board)):
            if board[i][num-1]!=0:
                doll=board[i][num-1]
                board[i][num-1]=0
                break
        #board에 인형이 없을 경우 moves의 다음으로 넘어간다
        if doll==0:
            continue
        #뽑힌 인형이 있는 stack에서 가장 최신에 뽑힌 인형을 updoll에 입력한다    
        updoll=stack.pop()
        #뽑은 인형과 이전에 뽑은 인형이 있다면 결과값에 두 인형의 개수를 더한다
        if updoll==doll:
            answer+=2
        # 다르다면 두 인형을 다시 stack에 저장한다
        else:
            stack.append(updoll)
            stack.append(doll)

    return answer