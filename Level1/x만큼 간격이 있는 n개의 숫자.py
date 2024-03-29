# https://school.programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = [x*(i+1) for i in range(n)]
    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))


# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.04ms, 10.2MB)
# 테스트 5 〉	통과 (0.04ms, 10.4MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.07ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
# 테스트 9 〉	통과 (0.09ms, 10.3MB)
# 테스트 10 〉	통과 (0.00ms, 10.1MB)
# 테스트 11 〉	통과 (0.06ms, 10.4MB)
# 테스트 12 〉	통과 (0.05ms, 10.3MB)
# 테스트 13 〉	통과 (0.09ms, 10.3MB)
# 테스트 14 〉	통과 (0.09ms, 10.4MB)