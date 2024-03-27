# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    who_report, report_cnt, callback_cnt = set(), {k:0 for k in id_list}, {k:0 for k in id_list}
    select = set()
    
    for rep in report:
        a, b = rep.split()
        if (a, b) not in who_report:
            report_cnt[b] += 1
            who_report.add((a, b))
            if report_cnt[b] >= k:
                select.add(b)
            
    for a, b in who_report:
        if b in select:
            callback_cnt[a] += 1
            
    return [x for x in callback_cnt.values()]

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# [2, 1, 1, 0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
# [0, 0]

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (263.06ms, 68.8MB)
# 테스트 4 〉	통과 (0.04ms, 10.4MB)
# 테스트 5 〉	통과 (0.04ms, 10.2MB)
# 테스트 6 〉	통과 (1.34ms, 10.6MB)
# 테스트 7 〉	통과 (2.79ms, 10.9MB)
# 테스트 8 〉	통과 (4.94ms, 11.4MB)
# 테스트 9 〉	통과 (148.45ms, 38MB)
# 테스트 10 〉	통과 (113.44ms, 38MB)
# 테스트 11 〉	통과 (283.20ms, 68.6MB)
# 테스트 12 〉	통과 (0.28ms, 10.3MB)
# 테스트 13 〉	통과 (0.26ms, 10.4MB)
# 테스트 14 〉	통과 (102.53ms, 31.5MB)
# 테스트 15 〉	통과 (234.39ms, 47.3MB)
# 테스트 16 〉	통과 (0.27ms, 10.2MB)
# 테스트 17 〉	통과 (0.33ms, 10.3MB)
# 테스트 18 〉	통과 (0.65ms, 10.3MB)
# 테스트 19 〉	통과 (1.31ms, 10.4MB)
# 테스트 20 〉	통과 (103.15ms, 31.7MB)
# 테스트 21 〉	통과 (228.33ms, 47.1MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.4MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)