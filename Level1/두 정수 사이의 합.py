# https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    a, b = [a, b] if a < b else [b, a]
    return b*(b+1) / 2 - a*(a-1) / 2

print(solution(3, 5))
# 12
print(solution(3, 3))
# 3
print(solution(5, 3))
# 12

# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.00ms, 9.99MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.1MB)
# 테스트 6 〉	통과 (0.00ms, 10.1MB)
# 테스트 7 〉	통과 (0.00ms, 10.1MB)
# 테스트 8 〉	통과 (0.00ms, 10.2MB)
# 테스트 9 〉	통과 (0.00ms, 9.99MB)
# 테스트 10 〉	통과 (0.00ms, 10MB)
# 테스트 11 〉	통과 (0.00ms, 10.1MB)
# 테스트 12 〉	통과 (0.00ms, 10.1MB)
# 테스트 13 〉	통과 (0.00ms, 10.1MB)
# 테스트 14 〉	통과 (0.00ms, 10.1MB)
# 테스트 15 〉	통과 (0.00ms, 10.2MB)
# 테스트 16 〉	통과 (0.00ms, 9.93MB)