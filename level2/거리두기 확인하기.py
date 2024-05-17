# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def check(place):
    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    dictionary = {'O': 0, 'P': 1}
    for row in range(5):
        for col in range(5):
            if place[row][col] in ['O', 'P']:
                temp = dictionary[place[row][col]]
                for dr, dc in moves:
                    nrow = row+dr
                    ncol = col+dc
                    if 0<=nrow<5 and 0<=ncol<5 and place[nrow][ncol] == 'P':
                        temp += 1
                        
                if temp >= 2:
                    return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        place = list(map(list, place))
        answer.append(check(place))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# [1, 0, 1, 1, 1]

# 테스트 1 〉	통과 (0.13ms, 10.2MB)
# 테스트 2 〉	통과 (0.07ms, 10.2MB)
# 테스트 3 〉	통과 (0.08ms, 10.2MB)
# 테스트 4 〉	통과 (0.07ms, 10.2MB)
# 테스트 5 〉	통과 (0.09ms, 10.3MB)
# 테스트 6 〉	통과 (0.10ms, 10.2MB)
# 테스트 7 〉	통과 (0.05ms, 10.2MB)
# 테스트 8 〉	통과 (0.05ms, 10.3MB)
# 테스트 9 〉	통과 (0.06ms, 10.3MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (0.07ms, 10.3MB)
# 테스트 12 〉	통과 (0.06ms, 10.2MB)
# 테스트 13 〉	통과 (0.04ms, 10.2MB)
# 테스트 14 〉	통과 (0.07ms, 10.2MB)
# 테스트 15 〉	통과 (0.06ms, 10.2MB)
# 테스트 16 〉	통과 (0.12ms, 10.3MB)
# 테스트 17 〉	통과 (0.06ms, 10.2MB)
# 테스트 18 〉	통과 (0.05ms, 10.2MB)
# 테스트 19 〉	통과 (0.04ms, 10.3MB)
# 테스트 20 〉	통과 (0.04ms, 10.2MB)
# 테스트 21 〉	통과 (0.04ms, 10.4MB)
# 테스트 22 〉	통과 (0.04ms, 10.2MB)
# 테스트 23 〉	통과 (0.06ms, 10.2MB)
# 테스트 24 〉	통과 (0.02ms, 10.4MB)
# 테스트 25 〉	통과 (0.15ms, 10.3MB)
# 테스트 26 〉	통과 (0.03ms, 10.2MB)
# 테스트 27 〉	통과 (0.04ms, 10.3MB)
# 테스트 28 〉	통과 (0.06ms, 10.3MB)
# 테스트 29 〉	통과 (0.09ms, 10.2MB)
# 테스트 30 〉	통과 (0.09ms, 10.1MB)
# 테스트 31 〉	통과 (0.07ms, 10.2MB)