# https://school.programmers.co.kr/learn/courses/30/lessons/135807

def inner(arr):
    arr = sorted(arr)
    a = arr[0]
    temp = set()
    for i in range(1, int(a**0.5)+1):
        if a % i == 0:
            temp.add(i)
            temp.add(a // i)
        
    result = set()
    for t in temp:
        for b in arr[1:]:
            if b % t != 0:
                break
        else:
            result.add(t)
            
    return result


def solution(arrayA, arrayB):
    arrayA_inner = inner(arrayA)
    arrayB_inner = inner(arrayB)
    
    canA, canB = [], []
    
    for A in arrayA_inner:
        for arrb in arrayB:
            if arrb % A == 0:
                break
        else:
            canA.append(A)
    
    for B in arrayB_inner:
        for arra in arrayA:
            if arra % B == 0:
                break
        else:
            canB.append(B)
    
    can = canA + canB
    if can:
        return max(can)
    return 0

print(solution([10, 17], [5, 20]))
# 0
print(solution([10, 20], [5, 17]))
# 10
print(solution([14, 35, 119], [18, 30, 102]))
# 7

# 테스트 1 〉	통과 (0.88ms, 10.4MB)
# 테스트 2 〉	통과 (1.67ms, 10.4MB)
# 테스트 3 〉	통과 (0.34ms, 10.3MB)
# 테스트 4 〉	통과 (24.98ms, 13.4MB)
# 테스트 5 〉	통과 (11.81ms, 10.6MB)
# 테스트 6 〉	통과 (13.76ms, 11.1MB)
# 테스트 7 〉	통과 (1.46ms, 10.3MB)
# 테스트 8 〉	통과 (3.09ms, 10.4MB)
# 테스트 9 〉	통과 (3.73ms, 10.7MB)
# 테스트 10 〉	통과 (0.47ms, 10.3MB)
# 테스트 11 〉	통과 (254.77ms, 56.2MB)
# 테스트 12 〉	통과 (419.19ms, 56.2MB)
# 테스트 13 〉	통과 (454.92ms, 56.2MB)
# 테스트 14 〉	통과 (196.07ms, 56.2MB)
# 테스트 15 〉	통과 (424.56ms, 56.2MB)
# 테스트 16 〉	통과 (638.33ms, 56.2MB)
# 테스트 17 〉	통과 (193.11ms, 56.2MB)
# 테스트 18 〉	통과 (249.51ms, 56.2MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.02ms, 10.2MB)
# 테스트 21 〉	통과 (0.02ms, 10.3MB)
# 테스트 22 〉	통과 (0.03ms, 10.3MB)
# 테스트 23 〉	통과 (0.05ms, 10.4MB)
# 테스트 24 〉	통과 (0.20ms, 10.3MB)
# 테스트 25 〉	통과 (1.60ms, 10.4MB)
# 테스트 26 〉	통과 (1.18ms, 10.3MB)
# 테스트 27 〉	통과 (0.11ms, 10.2MB)
# 테스트 28 〉	통과 (0.08ms, 10.4MB)
# 테스트 29 〉	통과 (0.03ms, 10.4MB)
# 테스트 30 〉	통과 (0.07ms, 10.4MB)
# 테스트 31 〉	통과 (0.03ms, 10.3MB)
# 테스트 32 〉	통과 (0.05ms, 10.3MB)
# 테스트 33 〉	통과 (0.27ms, 10.3MB)
# 테스트 34 〉	통과 (0.04ms, 10.3MB)
# 테스트 35 〉	통과 (0.06ms, 10.4MB)
# 테스트 36 〉	통과 (0.06ms, 10.4MB)