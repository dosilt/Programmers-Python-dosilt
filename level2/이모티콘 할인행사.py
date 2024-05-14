# https://school.programmers.co.kr/learn/courses/30/lessons/150368
# import sys
# sys.setrecursionlimit(10**6)

from collections import defaultdict
import math

def combi(arr, depth, max_len):
    for i in arr:
        if depth == max_len:
            yield [i]
        else:
            for j in combi(arr, depth+1, max_len):
                yield [i] + j


def market(users, sale_emoticons, candidate):
    pro, cash = 0, 0
    for per, max_price in users:
        temp = 0
        for n, candi in enumerate(candidate):
            if per <= candi:
                temp += sale_emoticons[candi][n]
                
        if temp >= max_price:
            pro += 1
        else:
            cash += temp
            
    return pro, cash

def solution(users, emoticons):
    sale_emoticons = defaultdict(list)
    for sale in [1, 2, 3, 4]:
        for emo in emoticons:
            sale_emoticons[sale].append(emo*(10-sale)/10)
    
    for i in range(len(users)):
        users[i][0] = math.ceil(users[i][0] / 10)
            
            
    candidates = list(combi([1, 2, 3, 4], 0, len(emoticons)-1))
    
    answer = []
    for candidate in candidates:
        pro, cash = market(users, sale_emoticons, candidate)
        answer.append([pro, cash])
        
    answer = sorted(answer, key=lambda x:[-x[0], -x[1]])
    return answer[0]

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
# [1, 5400]
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
# [4, 13860]

# 테스트 1 〉	통과 (0.07ms, 10.2MB)
# 테스트 2 〉	통과 (0.10ms, 10.2MB)
# 테스트 3 〉	통과 (0.39ms, 10.2MB)
# 테스트 4 〉	통과 (1.58ms, 10.2MB)
# 테스트 5 〉	통과 (2.89ms, 10.2MB)
# 테스트 6 〉	통과 (1.70ms, 10.4MB)
# 테스트 7 〉	통과 (15.86ms, 10.3MB)
# 테스트 8 〉	통과 (7.82ms, 10.3MB)
# 테스트 9 〉	통과 (61.71ms, 10.5MB)
# 테스트 10 〉	통과 (33.49ms, 11.6MB)
# 테스트 11 〉	통과 (298.51ms, 11.6MB)
# 테스트 12 〉	통과 (188.39ms, 16.3MB)
# 테스트 13 〉	통과 (1408.03ms, 16.7MB)
# 테스트 14 〉	통과 (1449.62ms, 16.7MB)
# 테스트 15 〉	통과 (67.50ms, 10.3MB)
# 테스트 16 〉	통과 (60.62ms, 10.6MB)
# 테스트 17 〉	통과 (0.39ms, 10.1MB)
# 테스트 18 〉	통과 (50.75ms, 10.4MB)
# 테스트 19 〉	통과 (0.11ms, 10.2MB)
# 테스트 20 〉	통과 (0.12ms, 10.2MB)