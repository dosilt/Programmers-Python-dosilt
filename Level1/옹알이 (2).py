# https://school.programmers.co.kr/learn/courses/30/lessons/133499


def check(bab, can_do):
    temp = []
    while True:
        for n, can in enumerate(can_do):
            if bab.startswith(can):
                if temp == []:
                    temp.append(n)
                elif temp[-1] != n:
                    temp.append(n)
                else:
                    return False
                bab = bab[len(can):]
                if bab == '':
                    return True
                break
        else:
            return False


def solution(babbling):
    can_do = ['aya', 'ye', 'woo', 'ma']
    
    answer = 0
    for bab in babbling:
        if check(bab, can_do):
            answer += 1
        pass
    return answer

print(solution(["aya", "yee", "u", "maa"]))
# 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
# 2

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.02ms, 10.2MB)
# 테스트 11 〉	통과 (0.05ms, 10.1MB)
# 테스트 12 〉	통과 (0.23ms, 10.2MB)
# 테스트 13 〉	통과 (0.11ms, 10.2MB)
# 테스트 14 〉	통과 (0.20ms, 10.2MB)
# 테스트 15 〉	통과 (0.10ms, 10.2MB)
# 테스트 16 〉	통과 (0.07ms, 10.2MB)
# 테스트 17 〉	통과 (0.33ms, 10.2MB)
# 테스트 18 〉	통과 (0.23ms, 10.3MB)
# 테스트 19 〉	통과 (0.02ms, 10.3MB)
# 테스트 20 〉	통과 (0.06ms, 10.3MB)