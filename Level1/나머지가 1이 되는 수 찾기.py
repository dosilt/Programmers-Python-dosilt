# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    n -= 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return i
    return n

print(solution(10))
# 3
print(solution(12))
# 11


# 테스트 1 〉	통과 (0.12ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	통과 (0.01ms, 10.4MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.02ms, 10.4MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)