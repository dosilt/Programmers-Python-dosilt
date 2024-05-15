# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        a, b = divmod(i, n)
        answer.append(max(a, b)+1)
    
    return answer

print(solution(3, 2, 5))
# [3, 2, 2, 3]
print(solution(4, 7, 14))
# [4, 3, 3, 3, 4, 4, 4, 4]

# 테스트 1 〉	통과 (26.90ms, 16.1MB)
# 테스트 2 〉	통과 (32.76ms, 18.8MB)
# 테스트 3 〉	통과 (30.05ms, 19.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.1MB)
# 테스트 6 〉	통과 (29.40ms, 18.3MB)
# 테스트 7 〉	통과 (33.37ms, 18.7MB)
# 테스트 8 〉	통과 (28.46ms, 17.4MB)
# 테스트 9 〉	통과 (44.03ms, 18.7MB)
# 테스트 10 〉	통과 (30.22ms, 18.6MB)
# 테스트 11 〉	통과 (31.64ms, 18.5MB)
# 테스트 12 〉	통과 (29.07ms, 17.8MB)
# 테스트 13 〉	통과 (30.03ms, 18.5MB)
# 테스트 14 〉	통과 (29.25ms, 18.2MB)
# 테스트 15 〉	통과 (29.99ms, 18MB)
# 테스트 16 〉	통과 (29.55ms, 18.3MB)
# 테스트 17 〉	통과 (35.60ms, 18.4MB)
# 테스트 18 〉	통과 (35.18ms, 18.9MB)
# 테스트 19 〉	통과 (32.93ms, 18.5MB)
# 테스트 20 〉	통과 (28.86ms, 18MB)