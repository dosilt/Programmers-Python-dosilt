# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    row, col = 0, 0
    for a, b in sizes:
        a, b = [a, b] if a > b else [b, a]
        row = max(a, row)
        col = max(b, col)
    return row*col

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
# 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
# 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
# 133

# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (0.00ms, 10.3MB)
# 테스트 3 〉	통과 (0.00ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.02ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.3MB)
# 테스트 10 〉	통과 (0.04ms, 10.2MB)
# 테스트 11 〉	통과 (0.08ms, 10.2MB)
# 테스트 12 〉	통과 (0.11ms, 10.1MB)
# 테스트 13 〉	통과 (0.36ms, 10.4MB)
# 테스트 14 〉	통과 (0.72ms, 10.4MB)
# 테스트 15 〉	통과 (1.20ms, 10.4MB)
# 테스트 16 〉	통과 (1.87ms, 10.6MB)
# 테스트 17 〉	통과 (3.17ms, 10.5MB)
# 테스트 18 〉	통과 (3.08ms, 10.8MB)
# 테스트 19 〉	통과 (3.36ms, 11.4MB)
# 테스트 20 〉	통과 (6.42ms, 11.4MB)