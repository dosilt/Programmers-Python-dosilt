# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def solution(k, ranges):
    arr = [k]
    while k > 1:
        if k % 2 == 0:
            k = k // 2
            arr.append(k)
        else:
            k = k * 3 + 1
            arr.append(k)
    
    area = []
    for i in range(len(arr)-1):
        area.append((arr[i] + arr[i+1]) / 2)
    
    answer = []
    for st, en in ranges:
        en += len(arr)-1
        
        if st <= en:
            answer.append(sum(area[st:en]))
        else:
            answer.append(-1.0)
    
    return answer

print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))
# [33.0, 31.5, 0.0, -1.0]
print(solution(3, [[0,0], [1,-2], [3,-3]]))
# [47.0, 36.0, 12.0]

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.21ms, 10.4MB)
# 테스트 3 〉	통과 (5.29ms, 12.1MB)
# 테스트 4 〉	통과 (0.58ms, 10.6MB)
# 테스트 5 〉	통과 (0.27ms, 10.4MB)
# 테스트 6 〉	통과 (1.34ms, 10.7MB)
# 테스트 7 〉	통과 (4.80ms, 12.1MB)
# 테스트 8 〉	통과 (5.68ms, 12.4MB)
# 테스트 9 〉	통과 (0.10ms, 10.2MB)
# 테스트 10 〉	통과 (1.70ms, 10.8MB)