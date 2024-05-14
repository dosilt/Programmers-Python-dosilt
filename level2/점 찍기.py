# https://school.programmers.co.kr/learn/courses/30/lessons/140107

def solution(k, d):
    answer = 0
    for y in range(0, d+1, k):
        x = int((d**2 - y**2)**0.5)
        
        a, b = divmod(x, k)
        answer += a + 1
    return answer

print(solution(2, 4))
# 6
print(solution(1, 5))
# 26

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10MB)
# 테스트 3 〉	통과 (2.48ms, 10.3MB)
# 테스트 4 〉	통과 (2.65ms, 10.1MB)
# 테스트 5 〉	통과 (3.68ms, 10.1MB)
# 테스트 6 〉	통과 (3.29ms, 10.3MB)
# 테스트 7 〉	통과 (1.74ms, 10.3MB)
# 테스트 8 〉	통과 (47.68ms, 10.3MB)
# 테스트 9 〉	통과 (3.60ms, 10MB)
# 테스트 10 〉	통과 (7.20ms, 10MB)
# 테스트 11 〉	통과 (1019.75ms, 10.3MB)
# 테스트 12 〉	통과 (0.02ms, 10.2MB)
# 테스트 13 〉	통과 (392.19ms, 10.4MB)
# 테스트 14 〉	통과 (260.93ms, 10.4MB)
# 테스트 15 〉	통과 (0.02ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10MB)