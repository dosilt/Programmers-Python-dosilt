# https://school.programmers.co.kr/learn/courses/30/lessons/12921


def even(n):
    temp = [False, False] + [True] * (n-1)
    for i in range(2, int(n**0.5)+1):
        if temp[i]:
            j = 2
            while i * j <= n:
                temp[i*j] = False
                j += 1
    return temp

def solution(n):
    temp = sum(even(n))
    return temp

print(solution(10))
# 4
print(solution(5))
# 3


# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.4MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.17ms, 10.2MB)
# 테스트 4 〉	통과 (0.27ms, 10.2MB)
# 테스트 5 〉	통과 (0.20ms, 10.2MB)
# 테스트 6 〉	통과 (2.25ms, 10.3MB)
# 테스트 7 〉	통과 (0.77ms, 10.2MB)
# 테스트 8 〉	통과 (1.56ms, 10.4MB)
# 테스트 9 〉	통과 (3.65ms, 10.2MB)
# 테스트 10 〉	통과 (127.05ms, 14.2MB)
# 테스트 11 〉	통과 (358.66ms, 23.4MB)
# 테스트 12 〉	통과 (142.37ms, 14.7MB)
# 효율성  테스트
# 테스트 1 〉	통과 (257.23ms, 24.2MB)
# 테스트 2 〉	통과 (246.75ms, 23.8MB)
# 테스트 3 〉	통과 (256.63ms, 24.2MB)
# 테스트 4 〉	통과 (270.79ms, 24MB