# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    word = word + 'B' * (5 - len(word))
    
    scores = [781, 156, 31, 6, 1]
    
    dictionary = {'A': '1', 'B': '0', 'E': '2', 'I': '3', 'O': '4', 'U': '5'}
    numbering = []
    for w in word:
        numbering.append(dictionary[w])
        
    answer = 0
    for i, n in enumerate(numbering):
        if n != '0':
            answer += 1 + scores[i] * (int(n)-1)
        else:
            continue
    return answer

print(solution("AAAAE"))
# 6
print(solution("AAAE"))
# 10
print(solution("I"))
# 1563
print(solution("EIO"))
# 1189

# 테스트 1 〉	통과 (0.02ms, 10.4MB)
# 테스트 2 〉	통과 (0.02ms, 10.5MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
# 테스트 7 〉	통과 (0.02ms, 10.5MB)
# 테스트 8 〉	통과 (0.02ms, 10.4MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.02ms, 10.4MB)
# 테스트 11 〉	통과 (0.03ms, 10.4MB)
# 테스트 12 〉	통과 (0.02ms, 10.4MB)
# 테스트 13 〉	통과 (0.02ms, 10.4MB)
# 테스트 14 〉	통과 (0.02ms, 10.4MB)
# 테스트 15 〉	통과 (0.02ms, 10.3MB)
# 테스트 16 〉	통과 (0.02ms, 10.3MB)
# 테스트 17 〉	통과 (0.02ms, 10.4MB)
# 테스트 18 〉	통과 (0.02ms, 10.4MB)
# 테스트 19 〉	통과 (0.02ms, 10.3MB)
# 테스트 20 〉	통과 (0.03ms, 10.3MB)
# 테스트 21 〉	통과 (0.02ms, 10.3MB)
# 테스트 22 〉	통과 (0.02ms, 10.2MB)
# 테스트 23 〉	통과 (0.03ms, 10.3MB)
# 테스트 24 〉	통과 (0.02ms, 10.4MB)
# 테스트 25 〉	통과 (0.03ms, 10.4MB)
# 테스트 26 〉	통과 (0.02ms, 10.4MB)
# 테스트 27 〉	통과 (0.03ms, 10.2MB)
# 테스트 28 〉	통과 (0.03ms, 10.4MB)
# 테스트 29 〉	통과 (0.02ms, 10.4MB)
# 테스트 30 〉	통과 (0.02ms, 10.3MB)
# 테스트 31 〉	통과 (0.02ms, 10.3MB)
# 테스트 32 〉	통과 (0.02ms, 10.3MB)
# 테스트 33 〉	통과 (0.02ms, 10.4MB)
# 테스트 34 〉	통과 (0.03ms, 10.5MB)
# 테스트 35 〉	통과 (0.02ms, 10.4MB)
# 테스트 36 〉	통과 (0.02ms, 10.4MB)
# 테스트 37 〉	통과 (0.02ms, 10.5MB)
# 테스트 38 〉	통과 (0.03ms, 10.4MB)
# 테스트 39 〉	통과 (0.02ms, 10.4MB)
# 테스트 40 〉	통과 (0.02ms, 10.3MB)