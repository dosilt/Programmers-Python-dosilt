# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    tile = brown + yellow
    for i in range(3, int(tile**0.5)+1):
        if (tile) % i == 0:
            if (i + tile//i) * 2 - 4 == brown:
                return [max(i, tile//i), min(i, tile//i)]

print(solution(10, 2))
# [4, 3]
print(solution(8, 1))
# [3, 3]
print(solution(24, 24))
# [8, 6]

# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.07ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.39ms, 10.3MB)
# 테스트 7 〉	통과 (0.10ms, 10.2MB)
# 테스트 8 〉	통과 (0.12ms, 10.3MB)
# 테스트 9 〉	통과 (0.07ms, 10.2MB)
# 테스트 10 〉	통과 (0.09ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)