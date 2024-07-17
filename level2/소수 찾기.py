# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def create_even(max_value):
    matrix = [False, False] + [True for _ in range(max_value-1)]
    
    for i in range(2, int((max_value+1)**0.5)+1):
        if matrix[i]:
            for j in range(i*2, max_value+1, i):
                matrix[j] = False
    return matrix

def solution(numbers):
    can_create = set()
    for i in range(1, len(numbers)+1):
        candidates = list(permutations(list(numbers), i))
        for candidate in candidates:
            number = int(''.join(candidate))
            if number > 1:
                can_create.add(number)

    can_create = sorted(list(can_create))
    
    temp = create_even(can_create[-1])
    answer = 0
    
    for c in can_create:
        answer += temp[c]
    return answer

print(solution("17"))
# 3
print(solution("011"))
# 2

# 테스트 1 〉	통과 (0.40ms, 10.4MB)
# 테스트 2 〉	통과 (95.45ms, 20.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (65.57ms, 15.1MB)
# 테스트 5 〉	통과 (756.14ms, 62.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
# 테스트 7 〉	통과 (0.41ms, 10.4MB)
# 테스트 8 〉	통과 (1270.62ms, 96.3MB)
# 테스트 9 〉	통과 (0.10ms, 10.3MB)
# 테스트 10 〉	통과 (138.89ms, 25.6MB)
# 테스트 11 〉	통과 (16.53ms, 11.8MB)
# 테스트 12 〉	통과 (10.87ms, 11.2MB)