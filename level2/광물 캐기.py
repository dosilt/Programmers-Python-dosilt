# https://school.programmers.co.kr/learn/courses/30/lessons/172927

import heapq

def calc(pick, mineral):
    score = 0
    for mine in mineral:
        score += pick[mine]
    return score


def solution(picks, minerals):
    minerals = minerals[:sum(picks)*5]
    
    dictionary = {'diamond': 25, 'iron': 5, 'stone': 1}
    dia_pick = {'diamond': 1, 'iron': 1, 'stone': 1}
    iron_pick = {'diamond': 5, 'iron': 1, 'stone': 1}
    stone_pick = {'diamond': 25, 'iron': 5, 'stone': 1}
    
    
    temp_score, temp_mineral = 0, []
    answer_list = []
    
    for mine in minerals:
        temp_mineral.append(mine)
        temp_score += dictionary[mine]
        if len(temp_mineral) == 5:
            heapq.heappush(answer_list, [-temp_score, temp_mineral])
            temp_mineral = []
            temp_score = 0
    else:    
        if temp_score != 0:
            heapq.heappush(answer_list, [-temp_score, temp_mineral])
        
    answer = 0
    while answer_list:
        temp = heapq.heappop(answer_list)
        if picks[0] != 0:
            answer += calc(dia_pick, temp[1])
            picks[0] -= 1
        elif picks[1] != 0:
            answer += calc(iron_pick, temp[1])
            picks[1] -= 1
        elif picks[2] != 0:
            answer += calc(stone_pick, temp[1])
            picks[2] -= 1
        else:
            return answer
    return answer

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
# 12
print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))
# 50
print(solution([0, 0, 1], ["stone", "stone", "stone", "stone", "stone", "diamond"]))
# 5
print(solution([0, 1, 0], ["stone","stone","stone","stone","stone"]))

print(solution([2, 1, 0], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "stone","stone","stone","stone","stone"]))

# 테스트 1 〉	통과 (0.02ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.03ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.3MB)
# 테스트 10 〉	통과 (0.02ms, 10.4MB)
# 테스트 11 〉	통과 (0.05ms, 10.3MB)
# 테스트 12 〉	통과 (0.03ms, 10.3MB)
# 테스트 13 〉	통과 (0.03ms, 10.3MB)
# 테스트 14 〉	통과 (0.03ms, 10.3MB)
# 테스트 15 〉	통과 (0.03ms, 10.4MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.02ms, 10.4MB)
# 테스트 18 〉	통과 (0.02ms, 10.3MB)
# 테스트 19 〉	통과 (0.03ms, 10.2MB)
# 테스트 20 〉	통과 (0.02ms, 10.4MB)
# 테스트 21 〉	통과 (0.02ms, 10.3MB)
# 테스트 22 〉	통과 (0.02ms, 10.3MB)
# 테스트 23 〉	통과 (0.03ms, 10.4MB)
# 테스트 24 〉	통과 (0.03ms, 10.3MB)
# 테스트 25 〉	통과 (0.05ms, 10.4MB)
# 테스트 26 〉	통과 (0.03ms, 10.3MB)
# 테스트 27 〉	통과 (0.03ms, 10.3MB)
# 테스트 28 〉	통과 (0.05ms, 10.4MB)
# 테스트 29 〉	통과 (0.03ms, 10.3MB)
# 테스트 30 〉	통과 (0.03ms, 10.4MB)
# 테스트 31 〉	통과 (0.02ms, 10.3MB)
# 테스트 32 〉	통과 (0.03ms, 10.3MB)
# 테스트 33 〉	통과 (0.03ms, 10.4MB)
# 테스트 34 〉	통과 (0.03ms, 10.3MB)
# 테스트 35 〉	통과 (0.03ms, 10.3MB)