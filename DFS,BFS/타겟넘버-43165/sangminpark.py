def solution(numbers, target):
    def DFS(index, current_sum):
        global output
        if index == len(numbers):
            if current_sum == target:
                output += 1
            return
        add_case = DFS(index + 1, current_sum + numbers[index])
        sub_case = DFS(index + 1, current_sum - numbers[index])
    DFS(0, 0)

    return output

output = 0
