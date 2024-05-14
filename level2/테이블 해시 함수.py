# https://school.programmers.co.kr/learn/courses/30/lessons/147354


def solution(data, col, row_begin, row_end):
    data = sorted(data, key=lambda x:[x[col-1], -x[0]])
    temp = []
    for row in range(row_begin-1, row_end):
        t = 0
        for d in data[row]:
            t += d % (row+1)
        temp.append(t)
        
    answer = temp[0]
    
    for t in temp[1:]:
        answer = answer ^ t
    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))
# 4

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.3MB)
# 테스트 4 〉	통과 (0.16ms, 10.3MB)
# 테스트 5 〉	통과 (1.19ms, 12.1MB)
# 테스트 6 〉	통과 (28.78ms, 57.8MB)
# 테스트 7 〉	통과 (38.76ms, 64.5MB)
# 테스트 8 〉	통과 (60.47ms, 64.5MB)
# 테스트 9 〉	통과 (50.43ms, 64.4MB)
# 테스트 10 〉	통과 (84.67ms, 64.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)