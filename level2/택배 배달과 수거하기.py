# https://school.programmers.co.kr/learn/courses/30/lessons/150369

def moves(cap, cur_point, arr):
    while cur_point > 0:
        if arr[cur_point] <= cap:
            cap -= arr[cur_point]
            arr[cur_point] = 0
            cur_point -= 1
        else:
            arr[cur_point] -= cap
            break
    return arr, cur_point

def solution(cap, n, deliveries, pickups):
    deliveries = [0] + deliveries
    pickups = [0] + pickups
    
    deliver_n, pickup_n = 0, 0
    for i in range(n, -1, -1):
        if deliveries[i] > 0:
            deliver_n = i
            break
            
    for i in range(n, -1, -1):
        if pickups[i] > 0:
            pickup_n = i
            break
            
    answer = 0
    
    while deliver_n != 0 or pickup_n != 0:
        answer += max(deliver_n, pickup_n) * 2
        deliveries, deliver_n = moves(cap, deliver_n, deliveries)
        pickups, pickup_n = moves(cap, pickup_n, pickups)
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
# 16
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
# 30

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.04ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.53ms, 10.3MB)
# 테스트 8 〉	통과 (1.76ms, 10.5MB)
# 테스트 9 〉	통과 (7.10ms, 10.4MB)
# 테스트 10 〉	통과 (5.39ms, 10.1MB)
# 테스트 11 〉	통과 (2.49ms, 10.4MB)
# 테스트 12 〉	통과 (2.22ms, 10.4MB)
# 테스트 13 〉	통과 (1.66ms, 10.3MB)
# 테스트 14 〉	통과 (2.49ms, 10.4MB)
# 테스트 15 〉	통과 (32.40ms, 13MB)
# 테스트 16 〉	통과 (1808.68ms, 12.9MB)
# 테스트 17 〉	통과 (207.99ms, 13MB)
# 테스트 18 〉	통과 (68.38ms, 13MB)
# 테스트 19 〉	통과 (52.95ms, 12.9MB)
# 테스트 20 〉	통과 (53.72ms, 12.9MB)