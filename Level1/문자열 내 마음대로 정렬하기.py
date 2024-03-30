# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    return sorted(strings, key=lambda x: [x[n], x])

print(solution(["sun", "bed", "car"], 1))
# ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))
# ["abcd", "abce", "cdx"]

# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 9.94MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.05ms, 10MB)