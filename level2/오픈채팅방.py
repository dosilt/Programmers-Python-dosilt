# https://school.programmers.co.kr/learn/courses/30/lessons/42888

from collections import defaultdict

def solution(record):
    dictionary = defaultdict(str)
    enter_list = []
    for rec in record:
        splited = rec.split()
        if len(splited) == 2:
            act, id_ = splited
            name = ''
        else:
            act, id_, name = splited
        
        if act != 'Change':
            enter_list.append([act, id_])
            
        if act in ['Change', 'Enter']:
            dictionary[id_] = name
            
    answer = []
    for act, id_ in enter_list:
        if act == 'Enter':
            temp = f'{dictionary[id_]}님이 들어왔습니다.'
        else:
            temp = f'{dictionary[id_]}님이 나갔습니다.'
        answer.append(temp)
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.06ms, 10.3MB)
# 테스트 4 〉	통과 (0.06ms, 10.1MB)
# 테스트 5 〉	통과 (1.08ms, 10.4MB)
# 테스트 6 〉	통과 (0.91ms, 10.4MB)
# 테스트 7 〉	통과 (1.03ms, 10.3MB)
# 테스트 8 〉	통과 (0.72ms, 10.3MB)
# 테스트 9 〉	통과 (1.26ms, 10.6MB)
# 테스트 10 〉	통과 (1.21ms, 10.3MB)
# 테스트 11 〉	통과 (0.67ms, 10.3MB)
# 테스트 12 〉	통과 (0.60ms, 10.4MB)
# 테스트 13 〉	통과 (1.10ms, 10.3MB)
# 테스트 14 〉	통과 (0.85ms, 10.4MB)
# 테스트 15 〉	통과 (0.02ms, 10.4MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.12ms, 10.1MB)
# 테스트 18 〉	통과 (0.06ms, 10.3MB)
# 테스트 19 〉	통과 (0.76ms, 10.5MB)
# 테스트 20 〉	통과 (0.57ms, 10.4MB)
# 테스트 21 〉	통과 (0.84ms, 10.3MB)
# 테스트 22 〉	통과 (0.57ms, 10.2MB)
# 테스트 23 〉	통과 (1.25ms, 10.6MB)
# 테스트 24 〉	통과 (0.76ms, 10.5MB)
# 테스트 25 〉	통과 (111.23ms, 44.9MB)
# 테스트 26 〉	통과 (151.47ms, 49.3MB)
# 테스트 27 〉	통과 (150.38ms, 53MB)
# 테스트 28 〉	통과 (153.49ms, 54.8MB)
# 테스트 29 〉	통과 (163.62ms, 54.7MB)
# 테스트 30 〉	통과 (105.89ms, 44.6MB)
# 테스트 31 〉	통과 (99.73ms, 52.7MB)
# 테스트 32 〉	통과 (85.15ms, 47.5MB)