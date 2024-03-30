# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = [arr[0]]
    for a in arr[1:]:
        if a == answer[-1]:
            continue
        answer.append(a)
    return answer

print(solution([1, 1, 3, 3, 0, 1, 1]))
# [1, 3, 0, 1]
print(solution([4, 4, 4, 3, 3]))
# [4, 3]


# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.02ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 9.98MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 9.93MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.1MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.00ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (61.30ms, 32.5MB)
# 테스트 2 〉	통과 (61.72ms, 32.4MB)
# 테스트 3 〉	통과 (59.73ms, 32.5MB)
# 테스트 4 〉	통과 (66.71ms, 32.5MB)