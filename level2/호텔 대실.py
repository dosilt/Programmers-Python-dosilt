# https://school.programmers.co.kr/learn/courses/30/lessons/155651

import heapq

def solution(book_time):
    book_min = []
    room = []
    for st, en in book_time:
        sh, sm = list(map(int, st.split(':')))
        eh, em = list(map(int, en.split(':')))
        heapq.heappush(book_min, [sh*60+sm, eh*60+em])
        
    while book_min:
        st, en = heapq.heappop(book_min)
        if room == []:
            room.append(en+10)
            
        else:
            for i in range(len(room)):
                if room[i] <= st:
                    room[i] = en+10
                    break
            else:
                room.append(en+10)
    return len(room)
        
        
        
        
        

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
# 3
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
# 1
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))
# 3

# 테스트 1 〉	통과 (0.07ms, 10.4MB)
# 테스트 2 〉	통과 (0.68ms, 10.3MB)
# 테스트 3 〉	통과 (7.12ms, 10.6MB)
# 테스트 4 〉	통과 (3.07ms, 10.5MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (10.85ms, 10.5MB)
# 테스트 7 〉	통과 (8.33ms, 10.6MB)
# 테스트 8 〉	통과 (1.68ms, 10.4MB)
# 테스트 9 〉	통과 (1.70ms, 10.5MB)
# 테스트 10 〉	통과 (3.74ms, 10.5MB)
# 테스트 11 〉	통과 (9.87ms, 10.7MB)
# 테스트 12 〉	통과 (7.81ms, 10.7MB)
# 테스트 13 〉	통과 (0.61ms, 10.5MB)
# 테스트 14 〉	통과 (5.79ms, 10.6MB)
# 테스트 15 〉	통과 (7.55ms, 10.6MB)
# 테스트 16 〉	통과 (1.69ms, 10.5MB)
# 테스트 17 〉	통과 (8.56ms, 10.6MB)
# 테스트 18 〉	통과 (4.39ms, 10.5MB)
# 테스트 19 〉	통과 (26.21ms, 10.6MB)