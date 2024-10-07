def solution(progresses, speeds):
    answer = []
    
    stack = []
    total = zip(progresses, speeds)
    
    # 일단 며칠 걸리는지 다 계산해서 순서대로 출력
    for pro, spe in total:
        cnt = 0
        while pro < 100:
            pro += spe
            cnt += 1
        stack.append(cnt)
    
    count = 1
    pivot = stack[0]
    # 뒤에 있는 수가 앞에 있는 수보다 작으면 앞 수로 만들고 같이 출력 
    for i in range(1, len(stack)):
        if stack[i] <= pivot:
            count += 1  # 현재 작업이 기준 일자보다 빨리 완료되므로 함께 배포
        else:
            answer.append(count)  # 지금까지 카운트된 작업들 배포
            pivot = stack[i]  # 기준 일자를 현재 작업으로 변경
            count = 1  # 카운트를 초기화하고 다시 시작
            
    answer.append(count)
    return answer
