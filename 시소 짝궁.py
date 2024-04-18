# https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import Counter

def solution(weights):
    answer = 0
    
    weights_cnt = Counter(weights)
    dictionary = {w: {w/2, w/3, w/4} for w in weights_cnt.keys()}
    candidates = list(dictionary.keys())
    lengths = len(candidates)
    
    for i in range(lengths):
        for j in range(i+1, lengths):
            if dictionary[candidates[i]].intersection(dictionary[candidates[j]]):
                answer += weights_cnt[candidates[i]] * weights_cnt[candidates[j]]
    
    for candidate in candidates:
        if weights_cnt[candidate] > 1:
            answer += weights_cnt[candidate] * (weights_cnt[candidate] - 1) / 2
    
    return answer

print(solution([100, 180, 360, 100, 270]))
# 4

# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (96.97ms, 10.8MB)
# 테스트 5 〉	통과 (127.92ms, 10.8MB)
# 테스트 6 〉	통과 (93.35ms, 11.4MB)
# 테스트 7 〉	통과 (94.43ms, 11.6MB)
# 테스트 8 〉	통과 (95.09ms, 12.2MB)
# 테스트 9 〉	통과 (117.18ms, 13MB)
# 테스트 10 〉	통과 (97.10ms, 13.8MB)
# 테스트 11 〉	통과 (97.61ms, 13.7MB)
# 테스트 12 〉	통과 (7.00ms, 13.9MB)
# 테스트 13 〉	통과 (6.42ms, 14.1MB)
# 테스트 14 〉	통과 (6.40ms, 14MB)
# 테스트 15 〉	통과 (6.98ms, 14MB)
# 테스트 16 〉	통과 (0.03ms, 10.2MB)
# 테스트 17 〉	통과 (0.04ms, 10.3MB)