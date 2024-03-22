# https://school.programmers.co.kr/learn/courses/30/lessons/250137

def healing(cur_health, health, bandage, remain):
    cur_health += bandage[1]
    if remain == bandage[0]:
        cur_health += bandage[2]
        remain = 0
    return min(cur_health, health), remain
    
    
def solution(bandage, health, attacks):
    monster_attack = 0
    cur_time, remain = 0, 0
    cur_health = health
    
    ## 공격 시간이 1000까지라서 다 돌아도 될 거라 판단
    while monster_attack < len(attacks):
        cur_time += 1
        if cur_time < attacks[monster_attack][0]:
            remain += 1
            cur_health, remain = healing(cur_health, health, bandage, remain)
        
        else:
            remain = 0
            cur_health -= attacks[monster_attack][1]
            monster_attack += 1
        
        if cur_health <= 0:
            return -1
    return cur_health

print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])) # 5
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])) # -1
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])) # -1
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]])) # 3

# 테스트 1 〉	통과 (0.05ms, 10.3MB)
# 테스트 2 〉	통과 (0.06ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.25ms, 10.3MB)
# 테스트 8 〉	통과 (0.05ms, 10.2MB)
# 테스트 9 〉	통과 (0.20ms, 10.1MB)
# 테스트 10 〉	통과 (0.06ms, 10.1MB)
# 테스트 11 〉	통과 (0.49ms, 10.2MB)
# 테스트 12 〉	통과 (0.35ms, 10.1MB)
# 테스트 13 〉	통과 (0.66ms, 10.3MB)
# 테스트 14 〉	통과 (0.50ms, 10.1MB)
# 테스트 15 〉	통과 (0.52ms, 10.3MB)
# 테스트 16 〉	통과 (0.42ms, 10.3MB)
# 테스트 17 〉	통과 (0.21ms, 10.1MB)
# 테스트 18 〉	통과 (0.52ms, 10.1MB)
# 테스트 19 〉	통과 (0.98ms, 10.1MB)
# 테스트 20 〉	통과 (0.55ms, 10.1MB)