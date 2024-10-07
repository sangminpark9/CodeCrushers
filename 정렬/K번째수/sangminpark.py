def solution(array, commands):
    answer = []
    for cmd in commands:
        first = cmd[0] -1
        last = cmd[1] -1
        point = cmd[2] -1
        tmp = array[first:last + 1]        
        tmp = sorted(tmp)
        answer.append(tmp[point])

    return answer
