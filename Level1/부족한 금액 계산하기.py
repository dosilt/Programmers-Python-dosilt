# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    need = money - sum([price * (x+1) for x in range(count)])
    return -need if need < 0 else 0

print(solution(3, 20, 4))
# 10

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (0.08ms, 10.3MB)
# 테스트 12 〉	통과 (0.14ms, 10.2MB)
# 테스트 13 〉	통과 (0.13ms, 10.2MB)
# 테스트 14 〉	통과 (0.18ms, 10.3MB)
# 테스트 15 〉	통과 (0.10ms, 10.3MB)
# 테스트 16 〉	통과 (0.13ms, 10.2MB)
# 테스트 17 〉	통과 (0.13ms, 10.2MB)
# 테스트 18 〉	통과 (0.36ms, 10.4MB)
# 테스트 19 〉	통과 (0.24ms, 10.4MB)
# 테스트 20 〉	통과 (0.25ms, 10.4MB)
# 테스트 21 〉	통과 (0.39ms, 10.3MB)
# 테스트 22 〉	통과 (0.40ms, 10.3MB)
# 테스트 23 〉	통과 (0.08ms, 10.4MB)