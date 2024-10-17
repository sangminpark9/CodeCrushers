def solution(brown, yellow):
    answer = []
    total = brown + yellow
    arr = []
    for i in range(1, total + 1): # 1부터 total
        if total % i == 0:
            row, col = total//i, i
            cal = (row*2) + ((col - 2) * 2)
            if cal == brown:
                return [row,col]
            arr.append((row, cal))
            
    
        
    return answer
