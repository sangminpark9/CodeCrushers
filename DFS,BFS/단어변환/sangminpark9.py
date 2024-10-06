from collections import deque
    
def solution(begin, target, words):
    if target not in words: return 0
    
    def can_change(word1, word2):
        output = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                output += 1
        return True if output == 1 else False
    
    q = deque()
    q.append((begin,0))
    visited = set()

    while q:
        current_word, steps = q.popleft()
        if current_word == target:
            return steps
        
        for word in words:
            if word not in visited and can_change(current_word, word):
                visited.add((word, steps + 1))
                q.append((word,steps+1))
    
    return 0


begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))
