# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter

def solution(topping):
    counter = Counter(topping)
    right_top = len(counter.keys())
    left = set()
    answer = 0
    for t in topping:
        left.add(t)
        counter[t] -= 1
        
        if counter[t] == 0:
            del counter[t]
            right_top -= 1
        
        if len(left) == right_top:
            answer += 1
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
# 2
print(solution([1, 2, 3, 1, 4]))
# 0


# 테스트 1 〉	통과 (4.74ms, 10.5MB)
# 테스트 2 〉	통과 (89.37ms, 14.8MB)
# 테스트 3 〉	통과 (76.28ms, 10.8MB)
# 테스트 4 〉	통과 (47.54ms, 10.9MB)
# 테스트 5 〉	통과 (521.79ms, 18.7MB)
# 테스트 6 〉	통과 (784.83ms, 51.3MB)
# 테스트 7 〉	통과 (810.67ms, 51.4MB)
# 테스트 8 〉	통과 (753.01ms, 51.2MB)
# 테스트 9 〉	통과 (655.21ms, 50.5MB)
# 테스트 10 〉	통과 (746.88ms, 50.5MB)
# 테스트 11 〉	통과 (74.12ms, 10.9MB)
# 테스트 12 〉	통과 (11.49ms, 11.3MB)
# 테스트 13 〉	통과 (660.28ms, 50.5MB)
# 테스트 14 〉	통과 (801.77ms, 50.4MB)
# 테스트 15 〉	통과 (628.77ms, 50.6MB)
# 테스트 16 〉	통과 (645.90ms, 50.6MB)
# 테스트 17 〉	통과 (618.22ms, 50.5MB)
# 테스트 18 〉	통과 (703.94ms, 51.3MB)
# 테스트 19 〉	통과 (696.69ms, 51.4MB)
# 테스트 20 〉	통과 (771.85ms, 51.3MB)