## https://school.programmers.co.kr/learn/courses/30/lessons/258712

def present_history(a, matrix, score):
    result = []
    for b in range(len(matrix)):
        if a == b:
            continue
        
        # a -> b 가 b -> a 보다 크면 a가 받아야됨
        if matrix[a][b] > matrix[b][a]:
            result.append(1)
        elif matrix[a][b] < matrix[b][a]:
            result.append(0)
        
        # a -> b == b -> a 같으면 score 봐야됨
        # score map [a] > [b] 면 a 가 받아야됨
        else:
            if score[a] > score[b]:
                result.append(1)
            else:
                result.append(0)
            
    return sum(result)


def solution(friends, gifts):
    name_map = {name: num for num, name in enumerate(friends)}
    matrix = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    score = [0 for _ in range(len(friends))]
    
    for gift in gifts:
        a, b = gift.split()
        
        # a가 b한테 준 선물
        matrix[name_map[a]][name_map[b]] += 1
        
        score[name_map[a]] += 1
        score[name_map[b]] -= 1
        
    answer = 0
    for i in range(len(friends)):
        answer = max(answer, present_history(i, matrix, score))
    
    return answer


print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
# 2
print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
# 4
print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]))
# 0

# 테스트 1 〉	통과 (0.04ms, 10.3MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (0.12ms, 10.3MB)
# 테스트 4 〉	통과 (0.12ms, 10.1MB)
# 테스트 5 〉	통과 (1.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.17ms, 10.4MB)
# 테스트 7 〉	통과 (1.18ms, 10.2MB)
# 테스트 8 〉	통과 (0.65ms, 10.4MB)
# 테스트 9 〉	통과 (2.73ms, 10.6MB)
# 테스트 10 〉	통과 (5.30ms, 10.4MB)
# 테스트 11 〉	통과 (2.88ms, 10.6MB)
# 테스트 12 〉	통과 (2.36ms, 10.5MB)
# 테스트 13 〉	통과 (6.38ms, 10.6MB)
# 테스트 14 〉	통과 (5.12ms, 10.7MB)
# 테스트 15 〉	통과 (6.31ms, 10.7MB)
# 테스트 16 〉	통과 (6.19ms, 11MB)
# 테스트 17 〉	통과 (0.09ms, 10.2MB)
# 테스트 18 〉	통과 (2.81ms, 10.7MB)
# 테스트 19 〉	통과 (7.59ms, 10.7MB)
# 테스트 20 〉	통과 (2.12ms, 10.4MB)