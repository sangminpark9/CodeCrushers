import collections

def solution(participant, completion):
    dic = collections.Counter(participant) - collections.Counter(completion)
    return list(dic.keys())[0]
