# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def check(x, y):
    if -5<=x<=5 and -5<=y<=5:
        return True
    return False


def solution(dirs):
    cx, cy, cnt = 0, 0, 0
    visited = set()
    for d in dirs:
        if d == 'U':
            nx, ny = cx, cy+1
            if check(nx, ny):
                if (cx, cy, nx, ny) not in visited:
                    cnt += 1
                visited.add((cx, cy, nx, ny))
                visited.add((nx, ny, cx, cy))
                cx, cy = nx, ny
                
        elif d == 'L':
            nx, ny = cx-1, cy
            if check(nx, ny):
                if (cx, cy, nx, ny) not in visited:
                    cnt += 1
                visited.add((cx, cy, nx, ny))
                visited.add((nx, ny, cx, cy))
                cx, cy = nx, ny
            
        elif d == 'R':
            nx, ny = cx+1, cy
            if check(nx, ny):
                if (cx, cy, nx, ny) not in visited:
                    cnt += 1
                visited.add((cx, cy, nx, ny))
                visited.add((nx, ny, cx, cy))
                cx, cy = nx, ny
                
        elif d == 'D':
            nx, ny = cx, cy-1
            if check(nx, ny):
                if (cx, cy, nx, ny) not in visited:
                    cnt += 1
                visited.add((cx, cy, nx, ny))
                visited.add((nx, ny, cx, cy))
                cx, cy = nx, ny
                
    return cnt

print(solution("ULURRDLLU"))
# 7
print(solution("LULLLLLLU"))
# 7


# 테스트 1 〉	통과 (0.04ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.08ms, 10.3MB)
# 테스트 5 〉	통과 (0.08ms, 10.2MB)
# 테스트 6 〉	통과 (0.04ms, 10.4MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.07ms, 10.3MB)
# 테스트 9 〉	통과 (0.04ms, 10.4MB)
# 테스트 10 〉	통과 (0.04ms, 10.2MB)
# 테스트 11 〉	통과 (0.04ms, 10.3MB)
# 테스트 12 〉	통과 (0.08ms, 10.3MB)
# 테스트 13 〉	통과 (0.07ms, 10.3MB)
# 테스트 14 〉	통과 (0.07ms, 10.2MB)
# 테스트 15 〉	통과 (0.07ms, 10.4MB)
# 테스트 16 〉	통과 (0.30ms, 10.2MB)
# 테스트 17 〉	통과 (0.31ms, 10.2MB)
# 테스트 18 〉	통과 (0.33ms, 10.2MB)
# 테스트 19 〉	통과 (0.33ms, 10.2MB)
# 테스트 20 〉	통과 (0.34ms, 10.2MB)