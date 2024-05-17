# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from copy import deepcopy
from collections import deque

def dfs(key, dictionary, visited, cur_point):
    while key:
        temp = key.popleft()
        
        for n in dictionary[temp]:
            if n not in visited:
                key.append(n)
                visited.add(n)
                cur_point += 1
    
    return visited, cur_point

def solution(n, wires):
    connect = []
    for i in range(len(wires)):
        temp = deepcopy(wires[:i] + wires[i+1:])
        dictionary = {i: [] for i in range(1, n+1)}
        cur_connect = []
        for a, b in temp:
            dictionary[a].append(b)
            dictionary[b].append(a)
        
        visited = set()
        for key in dictionary.keys():
            cur_point = 0
            if key not in visited:
                visited.add(key)
                cur_point += 1
                visited, cur_point = dfs(deque([key]), dictionary, visited, cur_point)
            
                cur_connect.append(cur_point)
        
        connect.append(cur_connect)
    return min([abs(a-b) for a, b in connect])

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# 3
print(solution(4, [[1,2],[2,3],[3,4]]))
# 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
# 1

# 테스트 1 〉	통과 (21.50ms, 10.3MB)
# 테스트 2 〉	통과 (23.02ms, 10.3MB)
# 테스트 3 〉	통과 (18.82ms, 10.3MB)
# 테스트 4 〉	통과 (18.45ms, 10.3MB)
# 테스트 5 〉	통과 (21.56ms, 10.3MB)
# 테스트 6 〉	통과 (0.06ms, 10.3MB)
# 테스트 7 〉	통과 (0.04ms, 10.3MB)
# 테스트 8 〉	통과 (1.14ms, 10.3MB)
# 테스트 9 〉	통과 (0.82ms, 10.4MB)
# 테스트 10 〉	통과 (19.29ms, 10.3MB)
# 테스트 11 〉	통과 (21.58ms, 10.3MB)
# 테스트 12 〉	통과 (19.09ms, 10.5MB)
# 테스트 13 〉	통과 (17.98ms, 10.3MB)