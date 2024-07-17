# https://school.programmers.co.kr/learn/courses/30/lessons/42860

from copy import deepcopy

def move(point, visited, max_len):
    for i in range(1, max_len):
        left = (point + i) % max_len
        right = (point - i + max_len) % max_len
        if visited[left] == 0:
            visited[left] = 1
            return left, visited, i
        elif visited[right] == 0:
            visited[right] = 1
            return right, visited, i
    
    return -1, visited, 0

def solution(name):
    visited, max_len = [], len(name)
    answer = 0
    for n in name:
        if n == 'A':
            visited.append(1)
        else:
            visited.append(0)
        downtop = ord(n) - ord('A')
        topdown = ord('Z') - ord(n) + 1
        answer += min(downtop, topdown)
        
    visited[0] = 1
    
    move_cnt = []
    for point in range(max_len):
        temp = point if point < max_len / 2 else max_len - point
        temp_visited = deepcopy(visited)
        temp_visited[point] = 1
        while point != -1:
            point, temp_visited, cnt = move(point, temp_visited, max_len)
            temp += cnt
        move_cnt.append(temp)
        
    return answer + min(move_cnt)

print(solution("JEROEN"))
# 56
print(solution("JAN"))
# 23

# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (0.07ms, 10.3MB)
# 테스트 3 〉	통과 (0.05ms, 10.3MB)
# 테스트 4 〉	통과 (0.13ms, 10.4MB)
# 테스트 5 〉	통과 (0.16ms, 10.2MB)
# 테스트 6 〉	통과 (0.12ms, 10.3MB)
# 테스트 7 〉	통과 (0.13ms, 10.4MB)
# 테스트 8 〉	통과 (0.04ms, 10.3MB)
# 테스트 9 〉	통과 (0.11ms, 10.3MB)
# 테스트 10 〉	통과 (0.12ms, 10.3MB)
# 테스트 11 〉	통과 (0.16ms, 10.4MB)
# 테스트 12 〉	통과 (0.21ms, 10.2MB)
# 테스트 13 〉	통과 (0.33ms, 10.3MB)
# 테스트 14 〉	통과 (0.24ms, 10.2MB)
# 테스트 15 〉	통과 (0.61ms, 10.3MB)
# 테스트 16 〉	통과 (0.02ms, 10.3MB)
# 테스트 17 〉	통과 (0.03ms, 10.3MB)
# 테스트 18 〉	통과 (0.20ms, 10.3MB)
# 테스트 19 〉	통과 (0.05ms, 10.2MB)
# 테스트 20 〉	통과 (0.26ms, 10.3MB)
# 테스트 21 〉	통과 (0.06ms, 10.3MB)
# 테스트 22 〉	통과 (0.14ms, 10.3MB)
# 테스트 23 〉	통과 (0.15ms, 10.2MB)
# 테스트 24 〉	통과 (0.13ms, 10.3MB)
# 테스트 25 〉	통과 (0.52ms, 10.4MB)
# 테스트 26 〉	통과 (0.10ms, 10.3MB)
# 테스트 27 〉	통과 (0.10ms, 10.4MB)