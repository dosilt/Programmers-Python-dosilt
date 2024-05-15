# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def dfs(energy, dungeons, visited, depth):
    global answer
    for n, (need, use) in enumerate(dungeons):
        if energy >= need and n not in visited:
            visited.add(n)
            dfs(energy - use, dungeons, visited, depth+1)
            visited.remove(n)
    else:
        answer = max(answer, depth)

def solution(k, dungeons):
    global answer
    answer = 0
    visited = set()
    dfs(k, dungeons, visited, 0)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))
# 3


# 테스트 1 〉	통과 (0.04ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.29ms, 10.3MB)
# 테스트 5 〉	통과 (2.03ms, 10.2MB)
# 테스트 6 〉	통과 (3.10ms, 10.2MB)
# 테스트 7 〉	통과 (19.14ms, 10.1MB)
# 테스트 8 〉	통과 (51.79ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (1.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.4MB)
# 테스트 12 〉	통과 (2.15ms, 10.3MB)
# 테스트 13 〉	통과 (0.28ms, 10.2MB)
# 테스트 14 〉	통과 (0.12ms, 10.1MB)
# 테스트 15 〉	통과 (0.04ms, 10.3MB)
# 테스트 16 〉	통과 (0.04ms, 10.2MB)
# 테스트 17 〉	통과 (0.10ms, 10.2MB)
# 테스트 18 〉	통과 (0.04ms, 10.2MB)
# 테스트 19 〉	통과 (0.09ms, 10.3MB)