# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    score_dict = {n: y for n, y in zip(name, yearning)}
    
    answer = []
    for pho in photo:
        temp = 0
        for p in pho:
            if p in set(score_dict.keys()):
                temp += score_dict[p]
        answer.append(temp)
    
    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
# [19, 15, 6]

print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
# [67, 0, 55]

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]))
# [5, 15, 0]


# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.45ms, 10.3MB)
# 테스트 4 〉	통과 (0.24ms, 10.1MB)
# 테스트 5 〉	통과 (3.20ms, 10.1MB)
# 테스트 6 〉	통과 (5.90ms, 10.1MB)
# 테스트 7 〉	통과 (6.12ms, 10.4MB)
# 테스트 8 〉	통과 (8.53ms, 10.4MB)
# 테스트 9 〉	통과 (10.83ms, 10.3MB)
# 테스트 10 〉	통과 (41.90ms, 10.6MB)
# 테스트 11 〉	통과 (22.36ms, 10.6MB)
# 테스트 12 〉	통과 (7.22ms, 10.6MB)
# 테스트 13 〉	통과 (0.14ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.4MB)