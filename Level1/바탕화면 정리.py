# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    board = list(map(list, wallpaper))
    
    files = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == '#':
                files.append([r, c])
    # left, right
    horizon = sorted(files, key=lambda x:x[0])
    vertical = sorted(files, key=lambda x:x[1])
    
    up = horizon[0]
    down = horizon[-1]
    left = vertical[0]
    right = vertical[-1]
    
    return [up[0], left[1], down[0]+1, right[1]+1]


print(solution([".#...", "..#..", "...#."]))
# [0, 1, 3, 4]
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
# [1, 3, 5, 8]
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]	))
# [0, 0, 7, 9]
print(solution(["..", "#."]))
# [1, 0, 2, 1]

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.1MB)
# 테스트 4 〉	통과 (0.05ms, 10.1MB)
# 테스트 5 〉	통과 (0.06ms, 10.2MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.14ms, 10MB)
# 테스트 8 〉	통과 (0.33ms, 10.2MB)
# 테스트 9 〉	통과 (0.76ms, 10.1MB)
# 테스트 10 〉	통과 (0.14ms, 10.2MB)
# 테스트 11 〉	통과 (0.09ms, 10.1MB)
# 테스트 12 〉	통과 (0.11ms, 10.4MB)
# 테스트 13 〉	통과 (0.11ms, 10.1MB)
# 테스트 14 〉	통과 (0.13ms, 10MB)
# 테스트 15 〉	통과 (0.13ms, 10.3MB)
# 테스트 16 〉	통과 (0.26ms, 10.2MB)
# 테스트 17 〉	통과 (0.08ms, 10.2MB)
# 테스트 18 〉	통과 (0.51ms, 10MB)
# 테스트 19 〉	통과 (0.20ms, 10.3MB)
# 테스트 20 〉	통과 (0.64ms, 10.2MB)
# 테스트 21 〉	통과 (0.02ms, 10.2MB)
# 테스트 22 〉	통과 (0.02ms, 10.2MB)
# 테스트 23 〉	통과 (0.05ms, 10.1MB)
# 테스트 24 〉	통과 (0.04ms, 10.1MB)
# 테스트 25 〉	통과 (0.21ms, 10.4MB)
# 테스트 26 〉	통과 (0.23ms, 10.2MB)
# 테스트 27 〉	통과 (0.15ms, 10.2MB)
# 테스트 28 〉	통과 (0.07ms, 10.1MB)
# 테스트 29 〉	통과 (0.21ms, 10.3MB)
# 테스트 30 〉	통과 (1.28ms, 10.3MB)
# 테스트 31 〉	통과 (0.35ms, 10.2MB)