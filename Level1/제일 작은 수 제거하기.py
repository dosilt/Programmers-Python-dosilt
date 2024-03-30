# https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    min_ = min(arr)
    answer = []
    for a in arr:
        if a == min_:
            pass
        else:
            answer.append(a)
    return answer

print(solution([4, 3, 2, 1]))
# [4, 3, 2]
print(solution([10]))
# [-1]


# 테스트 1 〉	통과 (7.01ms, 15.8MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.4MB)
# 테스트 4 〉	통과 (0.05ms, 10.1MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.06ms, 10.3MB)
# 테스트 7 〉	통과 (0.14ms, 10.3MB)
# 테스트 8 〉	통과 (0.00ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.00ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.03ms, 10MB)
# 테스트 14 〉	통과 (0.13ms, 10.3MB)
# 테스트 15 〉	통과 (0.03ms, 10.3MB)
# 테스트 16 〉	통과 (0.07ms, 10.3MB)