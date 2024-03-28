# https://school.programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution(participant, completion):
    parti = Counter(participant)
    compl = Counter(completion)
    
    for key in parti.keys():
        if parti[key] - compl[key] != 0:
            return key


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
# leo
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
# vinko
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
# mislav

# 정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.1MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.26ms, 10.2MB)
# 테스트 4 〉	통과 (0.47ms, 10.4MB)
# 테스트 5 〉	통과 (0.29ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.1MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (18.66ms, 24.2MB)
# 테스트 2 〉	통과 (44.61ms, 27.7MB)
# 테스트 3 〉	통과 (32.69ms, 30.1MB)
# 테스트 4 〉	통과 (52.95ms, 38.9MB)
# 테스트 5 〉	통과 (44.19ms, 38.9MB)