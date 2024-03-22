# https://school.programmers.co.kr/learn/courses/30/lessons/160586

from collections import defaultdict

def counter(target, dictionary):
    temp = 0
    for t in target:
        temp += dictionary[t]
        if dictionary[t] == 0:
            return -1
    return temp
    

def solution(keymap, targets):
    dictionary = defaultdict(int)
    for key in keymap:
        for n, k in enumerate(key):
            dictionary[k] = n+1 if dictionary[k] == 0 else min(dictionary[k], n+1)
            
    answer = []
    for target in targets:
        answer.append(counter(target, dictionary))
    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
# [9, 4]
print(solution(["AA"], ["B"]))
# [-1]
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))
# [4, 6]

# 테스트 1 〉	통과 (0.15ms, 10.3MB)
# 테스트 2 〉	통과 (0.14ms, 10.1MB)
# 테스트 3 〉	통과 (0.15ms, 10.2MB)
# 테스트 4 〉	통과 (0.18ms, 10.2MB)
# 테스트 5 〉	통과 (0.11ms, 10.2MB)
# 테스트 6 〉	통과 (0.19ms, 9.88MB)
# 테스트 7 〉	통과 (0.22ms, 10.2MB)
# 테스트 8 〉	통과 (0.15ms, 10.2MB)
# 테스트 9 〉	통과 (0.16ms, 10.1MB)
# 테스트 10 〉	통과 (0.17ms, 10.2MB)
# 테스트 11 〉	통과 (0.02ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.4MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (1.08ms, 10.2MB)
# 테스트 15 〉	통과 (1.32ms, 10.2MB)
# 테스트 16 〉	통과 (1.35ms, 10.2MB)
# 테스트 17 〉	통과 (1.48ms, 10.1MB)
# 테스트 18 〉	통과 (0.80ms, 10.2MB)
# 테스트 19 〉	통과 (1.26ms, 10.2MB)
# 테스트 20 〉	통과 (0.84ms, 10.2MB)
# 테스트 21 〉	통과 (1.30ms, 10.1MB)
# 테스트 22 〉	통과 (1.34ms, 10.3MB)
# 테스트 23 〉	통과 (2.03ms, 9.95MB)