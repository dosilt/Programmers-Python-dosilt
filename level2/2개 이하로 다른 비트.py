# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    for number in numbers:
        temp = '0' + bin(number)[2:]
        temp = list(temp[::-1])
        for i in range(len(temp)):
            if temp[i] == '0':
                temp[i] = '1'
                if i != 0:
                    temp[i-1] = '0'
                break
            else:
                continue
                
        answer.append(int(''.join(temp[::-1]), 2))
    return answer

print(solution([1, 2, 7, 16]))
# [3, 11]

# 테스트 1 〉	통과 (1.37ms, 10.3MB)
# 테스트 2 〉	통과 (159.30ms, 23MB)
# 테스트 3 〉	통과 (0.13ms, 10.2MB)
# 테스트 4 〉	통과 (1.16ms, 10.3MB)
# 테스트 5 〉	통과 (1.43ms, 10.5MB)
# 테스트 6 〉	통과 (1.25ms, 10.3MB)
# 테스트 7 〉	통과 (179.79ms, 22.3MB)
# 테스트 8 〉	통과 (180.83ms, 22.1MB)
# 테스트 9 〉	통과 (178.33ms, 21.8MB)
# 테스트 10 〉	통과 (390.94ms, 23.9MB)
# 테스트 11 〉	통과 (389.34ms, 23.8MB)