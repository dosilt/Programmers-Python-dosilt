# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def checker(arr, row, col, length, visited, answer):
    initial = arr[row][col] 
    for r in range(length):
        for c in range(length):
            if arr[row+r][col+c] == initial:
                continue
            else:
                return visited, answer
            
    for r in range(length):
        for c in range(length):
            visited[row+r][col+c] = True
    answer[initial] += 1
    return visited, answer
            
    

def solution(arr):
    length = len(arr)
    answer = [0, 0]
    
    visited = [[False for _ in range(length)] for _ in range(length)]
    while True:
        if length == 1:
            break
        
        for row in range(0, len(arr), length):
            for col in range(0, len(arr), length):
                if visited[row][col] is False:
                    visited, answer = checker(arr, row, col, length, visited, answer)
        
        length = length // 2
        
        
    for row in range(len(arr)):
        for col in range(len(arr)):
            if visited[row][col] is False:
                answer[arr[row][col]] += 1
    
    return answer

print(solution([[1]]))

print(solution([[1, 1], [1, 1]]))

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# [4, 9]
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
# [10, 15]

# 테스트 1 〉	통과 (0.26ms, 10.2MB)
# 테스트 2 〉	통과 (0.24ms, 10.1MB)
# 테스트 3 〉	통과 (0.20ms, 10.2MB)
# 테스트 4 〉	통과 (0.06ms, 10.2MB)
# 테스트 5 〉	통과 (80.27ms, 12.6MB)
# 테스트 6 〉	통과 (52.78ms, 12.6MB)
# 테스트 7 〉	통과 (49.08ms, 12.6MB)
# 테스트 8 〉	통과 (47.91ms, 12.6MB)
# 테스트 9 〉	통과 (44.64ms, 12.6MB)
# 테스트 10 〉	통과 (235.33ms, 20.7MB)
# 테스트 11 〉	통과 (0.05ms, 10.2MB)
# 테스트 12 〉	통과 (0.06ms, 10.1MB)
# 테스트 13 〉	통과 (41.72ms, 12.5MB)
# 테스트 14 〉	통과 (168.92ms, 20.5MB)
# 테스트 15 〉	통과 (171.31ms, 20.6MB)
# 테스트 16 〉	통과 (54.15ms, 12.6MB)