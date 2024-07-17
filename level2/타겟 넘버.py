# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def dfs(numbers):
    cur_point = [numbers[0], -numbers[0]]
    
    for i in numbers[1:]:
        temp = []
        for c in cur_point:
            temp.append(c + i)
            temp.append(c - i)
        
        cur_point = temp
    return cur_point

def solution(numbers, target):
    output = dfs(numbers)
    return output.count(target)

print(solution([1, 1, 1, 1, 1], 3))
# 5
print(solution([4, 1, 2, 1], 4))
# 2

# 테스트 1 〉	통과 (203.04ms, 50.1MB)
# 테스트 2 〉	통과 (218.91ms, 49.5MB)
# 테스트 3 〉	통과 (0.28ms, 10.3MB)
# 테스트 4 〉	통과 (0.64ms, 10.3MB)
# 테스트 5 〉	통과 (6.17ms, 11.1MB)
# 테스트 6 〉	통과 (0.54ms, 10.2MB)
# 테스트 7 〉	통과 (0.16ms, 10.2MB)
# 테스트 8 〉	통과 (2.90ms, 10.4MB)