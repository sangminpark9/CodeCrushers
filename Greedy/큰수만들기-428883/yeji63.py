def solution(number, k):
    stack = []
    for n in number:
        while k > 0 and stack and stack[-1] < n:
            stack.pop()
            k -= 1
            
        stack.append(n)
    
    if k!=0:
        stack.pop()
    
    return ''.join(stack)
    
    
    # number = 1231234  k = 3 (최종 4자리수, 0123에서 첫째자리 골라야함/ 뒤에 3자리수가 남아야해) return 3234
    #           1924       2 (최종 2자리수, 012에서 첫째자리 골라야함 / 뒤에 1자리수가 나마야해)   94
    #          41772 52841  4  (최종 6자리수, 01234에서 첫째자리 골라야함 / 뒤에 다섯자리수가 남아ㅑ해)  775841
    # 자릿수가 len(number)-k = 2
    # 뒤에 남아있어야 하는 수가 len-k-1
    # k+1 까지만 잘라서 그 중 max를 최대로 남김

