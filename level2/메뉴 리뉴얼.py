# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        total = []
        for order in orders:
            total.extend(list(combinations(order, c)))
            
        result = []
        for c in total:
            result.append(''.join(sorted(c)))
            
        temp = 2
        cur_answer = []
        for t in Counter(result).most_common():
            if t[1] >= temp:
                cur_answer.append(t[0])
                temp = t[1]
        answer.extend(cur_answer)
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
# ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
# ["WX", "XY"]


# 테스트 1 〉	통과 (0.08ms, 10.2MB)
# 테스트 2 〉	통과 (0.06ms, 10.1MB)
# 테스트 3 〉	통과 (0.08ms, 10.3MB)
# 테스트 4 〉	통과 (0.09ms, 10.2MB)
# 테스트 5 〉	통과 (0.09ms, 10.1MB)
# 테스트 6 〉	통과 (0.20ms, 10.2MB)
# 테스트 7 〉	통과 (0.20ms, 10.2MB)
# 테스트 8 〉	통과 (1.70ms, 10.5MB)
# 테스트 9 〉	통과 (0.99ms, 10.5MB)
# 테스트 10 〉	통과 (1.32ms, 10.5MB)
# 테스트 11 〉	통과 (0.75ms, 10.6MB)
# 테스트 12 〉	통과 (0.83ms, 10.6MB)
# 테스트 13 〉	통과 (1.27ms, 10.5MB)
# 테스트 14 〉	통과 (0.93ms, 10.5MB)
# 테스트 15 〉	통과 (1.33ms, 10.5MB)
# 테스트 16 〉	통과 (0.37ms, 10.4MB)
# 테스트 17 〉	통과 (0.25ms, 10.4MB)
# 테스트 18 〉	통과 (0.11ms, 10.3MB)
# 테스트 19 〉	통과 (0.05ms, 10.1MB)
# 테스트 20 〉	통과 (0.28ms, 10.4MB)