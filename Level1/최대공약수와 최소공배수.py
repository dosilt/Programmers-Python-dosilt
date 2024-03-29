# https://school.programmers.co.kr/learn/courses/30/lessons/12940

def mins_(a, b):
    while b:
        a, b = b, a%b
    return a

def solution(n, m):
    temp = mins_(n, m)
    return [temp, (n*m)//temp]


print(solution(3, 12))
# [3, 12]
print(solution(2, 5))
# [1, 10]

# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.1MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.1MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.1MB)
# 테스트 8 〉	통과 (0.00ms, 10.2MB)
# 테스트 9 〉	통과 (0.00ms, 10.2MB)
# 테스트 10 〉	통과 (0.00ms, 10.2MB)
# 테스트 11 〉	통과 (0.00ms, 10.3MB)
# 테스트 12 〉	통과 (0.00ms, 10.3MB)
# 테스트 13 〉	통과 (0.00ms, 10.1MB)
# 테스트 14 〉	통과 (0.00ms, 10.2MB)
# 테스트 15 〉	통과 (0.00ms, 10.2MB)
# 테스트 16 〉	통과 (0.00ms, 10.2MB)