# https://school.programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def check(relation, candidate, result):
    sample = set()
    for row in range(len(relation)):
        temp = ''
        for candi in candidate:
            temp += str(relation[row][candi])
        sample.add(temp)
        
    if len(sample) == len(relation):
        result.append(candidate)
    return result

def solution(relation):
    result = []
    for i in range(1, len(relation[0])+1):
        candidates = list(map(list, combinations(range(len(relation[0])), i)))
        
        for candidate in candidates:
            result = check(relation, candidate, result)
            
    answer = [result[0]]
    
    for r in result[1:]:
        for a in answer:
            if set(a).issubset(set(r)):
                break
        else:
            answer.append(r)
    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
# 2

# 테스트 1 〉	통과 (0.08ms, 10.4MB)
# 테스트 2 〉	통과 (0.08ms, 10.1MB)
# 테스트 3 〉	통과 (0.61ms, 10.2MB)
# 테스트 4 〉	통과 (0.08ms, 10.2MB)
# 테스트 5 〉	통과 (0.07ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.19ms, 10.3MB)
# 테스트 10 〉	통과 (0.16ms, 10.3MB)
# 테스트 11 〉	통과 (0.25ms, 10.3MB)
# 테스트 12 〉	통과 (1.86ms, 10.2MB)
# 테스트 13 〉	통과 (0.70ms, 10.4MB)
# 테스트 14 〉	통과 (0.07ms, 10.2MB)
# 테스트 15 〉	통과 (0.06ms, 10.3MB)
# 테스트 16 〉	통과 (0.09ms, 10.3MB)
# 테스트 17 〉	통과 (0.10ms, 10.2MB)
# 테스트 18 〉	통과 (5.33ms, 10.2MB)
# 테스트 19 〉	통과 (3.78ms, 10.3MB)
# 테스트 20 〉	통과 (8.56ms, 10.2MB)
# 테스트 21 〉	통과 (6.56ms, 10.2MB)
# 테스트 22 〉	통과 (2.58ms, 10.3MB)
# 테스트 23 〉	통과 (0.12ms, 10.2MB)
# 테스트 24 〉	통과 (1.89ms, 10.2MB)
# 테스트 25 〉	통과 (8.37ms, 10.4MB)
# 테스트 26 〉	통과 (5.45ms, 10.2MB)
# 테스트 27 〉	통과 (0.85ms, 10.2MB)
# 테스트 28 〉	통과 (1.09ms, 10.3MB)