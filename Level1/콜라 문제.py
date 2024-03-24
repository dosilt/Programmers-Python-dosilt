# https://school.programmers.co.kr/learn/courses/30/lessons/132267


def solution(a, b, n):
    answer = 0
    while n >= a:
        change, remain = divmod(n, a)
        change = change * b
        answer += change
        n = remain + change
        
    return answer

print(solution(2, 1, 20))
# 19
print(solution(3, 1, 20))
# 9 


# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.00ms, 10.3MB)
# 테스트 5 〉	통과 (0.00ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.1MB)
# 테스트 8 〉	통과 (0.00ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.00ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.49ms, 10.1MB)
# 테스트 13 〉	통과 (0.00ms, 10.1MB)
# 테스트 14 〉	통과 (0.00ms, 10.3MB)