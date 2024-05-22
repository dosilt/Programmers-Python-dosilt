# https://school.programmers.co.kr/learn/courses/30/lessons/62048

def maximum(a, b):
    while True:
        c, d = divmod(a, b)
        a = b
        b = d
        if d == 0:
            break
    return a

def solution(w,h):
    
    return w*h - w - h + maximum(w, h)

print(solution(8, 12))
# 80

# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.00ms, 10.3MB)
# 테스트 5 〉	통과 (0.00ms, 10.1MB)
# 테스트 6 〉	통과 (0.00ms, 10.1MB)
# 테스트 7 〉	통과 (0.00ms, 10.3MB)
# 테스트 8 〉	통과 (0.00ms, 10.3MB)
# 테스트 9 〉	통과 (0.00ms, 10.1MB)
# 테스트 10 〉	통과 (0.00ms, 10.2MB)
# 테스트 11 〉	통과 (0.00ms, 10.2MB)
# 테스트 12 〉	통과 (0.00ms, 10.3MB)
# 테스트 13 〉	통과 (0.00ms, 10.3MB)
# 테스트 14 〉	통과 (0.00ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.00ms, 10.3MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.00ms, 10.2MB)