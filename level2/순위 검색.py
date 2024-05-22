# https://school.programmers.co.kr/learn/courses/30/lessons/72412

from collections import defaultdict, Counter
from bisect import bisect_left, insort

def solution(info, query):
    dictionary = defaultdict(list)
    for i in info:
        lang, posi, career, food, score = i.split()
        for l in [lang, '-']:
            for p in [posi, '-']:
                for c in [career, '-']:
                    for f in [food, '-']:
                        # insort(dictionary[f'{l}-{p}-{c}-{f}'], int(score))
                        dictionary[f'{l}-{p}-{c}-{f}'].append(int(score))
                        
                        
    # 이진 탐색만 직접 구현
    # answer = []
    # for q in query:
    #     lang, _, posi, _, career, _, food, score = q.split()
    #     candidates = dictionary[f'{lang}-{posi}-{career}-{food}']
    #     candidates = sorted(candidates)
    #     temp = len(candidates) - bisect_left(candidates, int(score))
    #     answer.append(temp)
    
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
# [1,1,1,1,2,4]

# 정확성  테스트
# 테스트 1 〉	통과 (0.19ms, 10.4MB)
# 테스트 2 〉	통과 (0.33ms, 10.4MB)
# 테스트 3 〉	통과 (0.30ms, 10.3MB)
# 테스트 4 〉	통과 (1.11ms, 10.6MB)
# 테스트 5 〉	통과 (1.87ms, 10.4MB)
# 테스트 6 〉	통과 (4.20ms, 10.9MB)
# 테스트 7 〉	통과 (2.43ms, 10.6MB)
# 테스트 8 〉	통과 (37.13ms, 13.8MB)
# 테스트 9 〉	통과 (40.72ms, 15.5MB)
# 테스트 10 〉	통과 (38.81ms, 16.2MB)
# 테스트 11 〉	통과 (2.25ms, 10.4MB)
# 테스트 12 〉	통과 (4.41ms, 10.9MB)
# 테스트 13 〉	통과 (4.32ms, 10.8MB)
# 테스트 14 〉	통과 (35.58ms, 13.3MB)
# 테스트 15 〉	통과 (34.23ms, 13.3MB)
# 테스트 16 〉	통과 (2.07ms, 10.5MB)
# 테스트 17 〉	통과 (4.99ms, 10.8MB)
# 테스트 18 〉	통과 (32.17ms, 13.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (744.43ms, 84.4MB)
# 테스트 2 〉	통과 (652.71ms, 84MB)
# 테스트 3 〉	통과 (766.59ms, 83.3MB)
# 테스트 4 〉	통과 (765.03ms, 84.5MB)