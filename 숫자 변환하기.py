# https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque

def bfs(x, y, n):
    queue = deque([[x, 0]])
    visited = {x}
    while queue:
        cur_x, cnt = queue.popleft()
        
        if cur_x == y:
            return cnt
        
        if cur_x + n <= y and cur_x + n not in visited:
            queue.append([cur_x+n, cnt+1])
            visited.add(cur_x+n)
        
        if cur_x * 2 <= y and cur_x * 2 not in visited:
            queue.append([cur_x*2, cnt+1])
            visited.add(cur_x*2)

        if cur_x * 3 <= y and cur_x * 3 not in visited:
            queue.append([cur_x*3, cnt+1])
            visited.add(cur_x*3)
    return -1
            
def solution(x, y, n):
    answer = bfs(x, y, n)
    return answer

print(solution(10, 40, 5))
# 2
print(solution(10, 40, 30))
# 1
print(solution(2, 5, 4))
# -1

# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.00ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	통과 (78.24ms, 20.9MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (59.65ms, 20.9MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (592.41ms, 102MB)
# 테스트 10 〉	통과 (440.29ms, 68.4MB)
# 테스트 11 〉	통과 (187.71ms, 38.6MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.00ms, 10.3MB)
# 테스트 14 〉	통과 (5.38ms, 10.9MB)
# 테스트 15 〉	통과 (0.53ms, 10.4MB)
# 테스트 16 〉	통과 (1.39ms, 10.5MB)