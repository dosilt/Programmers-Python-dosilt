# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    ranking = {player: num for num, player in enumerate(players)}
    
    for calling in callings:
        cur_pos = ranking[calling]
        ranking[calling] -= 1
        ranking[players[cur_pos-1]] += 1
        players[cur_pos], players[cur_pos-1] = players[cur_pos-1], players[cur_pos]
    
    return players


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
# ["mumu", "kai", "mine", "soe", "poe"]

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (0.35ms, 10.2MB)
# 테스트 5 〉	통과 (2.40ms, 10.5MB)
# 테스트 6 〉	통과 (4.41ms, 10.7MB)
# 테스트 7 〉	통과 (23.70ms, 14.3MB)
# 테스트 8 〉	통과 (56.63ms, 18.7MB)
# 테스트 9 〉	통과 (132.53ms, 27.9MB)
# 테스트 10 〉	통과 (349.29ms, 56.7MB)
# 테스트 11 〉	통과 (730.16ms, 91.4MB)
# 테스트 12 〉	통과 (706.89ms, 91.6MB)
# 테스트 13 〉	통과 (1021.86ms, 91.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.1MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.1MB)