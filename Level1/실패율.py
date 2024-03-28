# https://school.programmers.co.kr/learn/courses/30/lessons/42889

from collections import Counter

def solution(N, stages):
    stage_cnt = Counter(stages)
    people = len(stages)
    score = {i+1: 0 for i in range(N)}
    
    for i in range(1, N+1):
        if people == 0:
            score[i] = 0
        else:
            score[i] = stage_cnt[i] / people
            people -= stage_cnt[i]
        
    return [a for a, b in sorted(score.items(), key=lambda x:[x[1], -x[0]], reverse=True)]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# [3, 4, 2, 1, 5]
print(solution(4, [4, 4, 4, 4, 4]))
# [4, 1, 2, 3]

# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (0.07ms, 10.1MB)
# 테스트 3 〉	통과 (1.11ms, 10.5MB)
# 테스트 4 〉	통과 (4.16ms, 10.8MB)
# 테스트 5 〉	통과 (12.58ms, 15MB)
# 테스트 6 〉	통과 (0.13ms, 10.2MB)
# 테스트 7 〉	통과 (0.43ms, 10.4MB)
# 테스트 8 〉	통과 (4.45ms, 10.9MB)
# 테스트 9 〉	통과 (12.79ms, 15.1MB)
# 테스트 10 〉	통과 (4.81ms, 10.9MB)
# 테스트 11 〉	통과 (4.89ms, 10.8MB)
# 테스트 12 〉	통과 (7.08ms, 11.5MB)
# 테스트 13 〉	통과 (7.58ms, 11.5MB)
# 테스트 14 〉	통과 (0.05ms, 10.2MB)
# 테스트 15 〉	통과 (3.04ms, 10.7MB)
# 테스트 16 〉	통과 (2.88ms, 10.3MB)
# 테스트 17 〉	통과 (2.96ms, 10.6MB)
# 테스트 18 〉	통과 (1.49ms, 10.3MB)
# 테스트 19 〉	통과 (0.32ms, 10.2MB)
# 테스트 20 〉	통과 (3.17ms, 10.3MB)
# 테스트 21 〉	통과 (7.91ms, 10.9MB)
# 테스트 22 〉	통과 (17.89ms, 18.3MB)
# 테스트 23 〉	통과 (17.16ms, 11.6MB)
# 테스트 24 〉	통과 (15.77ms, 11.7MB)
# 테스트 25 〉	통과 (0.03ms, 10.2MB)
# 테스트 26 〉	통과 (0.05ms, 10.3MB)
# 테스트 27 〉	통과 (0.03ms, 10.4MB)