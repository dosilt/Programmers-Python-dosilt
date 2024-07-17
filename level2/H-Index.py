# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    print(citations)
    
    for i in range(len(citations)):
        print(i, citations[i], i+1)
        if(citations[i] < i+1):
            return i

    return len(citations)   

print(solution([3, 0, 6, 1, 5]))
# 3

print(solution([0, 0, 1]))