# https://school.programmers.co.kr/learn/courses/30/lessons/49993

from collections import defaultdict

def checker(skill_tree, dictionary):
    cnt = 0
    for s in skill_tree:
        if dictionary[s] != 0:
            if dictionary[s] - cnt != 1:
                return 0
            cnt += 1
    return 1

def solution(skill, skill_trees):
    dictionary = defaultdict(int)
    for n, s in enumerate(skill):
        dictionary[s] = n+1
    
    answer = 0
    for skill_tree in skill_trees:
        answer += checker(skill_tree, dictionary)
        
    return answer

print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))
# 2

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.1MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.02ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.4MB)
# 테스트 7 〉	통과 (0.02ms, 10.4MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.02ms, 10.2MB)
# 테스트 14 〉	통과 (0.02ms, 10.1MB)