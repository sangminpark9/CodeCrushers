def solution(numbers):
    answer = 0
    arr = []
    def make_arr(current, remaining):
        if not remaining:
            if current != '' and str(int(current)) not in arr:
                    arr.append(str(int(current)))
            return
        for i in range(len(remaining)):
            n = remaining[i]
            new_remaining = remaining[:i] + remaining[i+1:]
            make_arr(current + n, new_remaining)
        if current != '' and str(int(current)) not in arr:
            arr.append(str(int(current)))
        
    make_arr('', numbers)
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    for n in arr:
        if n != '':
            n = str(int(n))
            if is_prime(int(n)):
                answer += 1

    return answer

numbers = "011"
print(solution(numbers))
