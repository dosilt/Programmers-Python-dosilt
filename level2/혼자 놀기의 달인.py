# https://school.programmers.co.kr/learn/courses/30/lessons/131130

def finding(cards, visited, cur_pos):
    result = [cur_pos]
    while visited[cur_pos] is False:
        visited[cur_pos] = True
        cur_pos = cards[cur_pos]
        result.append(cur_pos)
    return len(result)


def solution(cards):
    cards = [0] + cards
    visited = [False] * (len(cards)+1)
    candidates = []
    for i in range(1, len(cards)):
        if visited[i] is False:
            visited[i] = True
            result = finding(cards, visited, cards[i])
            candidates.append(result)
            
    candidates = sorted(candidates, reverse=True)
    if len(candidates) < 2:
        return 0
    return candidates[0] * candidates[1]

print(solution([8, 6, 3, 7, 2, 5, 1, 4]))
# 12

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.1MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.03ms, 10.1MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.04ms, 10.1MB)