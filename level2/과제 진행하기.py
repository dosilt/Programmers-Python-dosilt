# https://school.programmers.co.kr/learn/courses/30/lessons/176962

from collections import deque
import heapq

def solution(plans):
    heap_queue, stack = [], deque()
    
    for subject, start, duration in plans:
        h, m = list(map(int, start.split(':')))
        start_time = h * 60 + m
        end_time = start_time + int(duration)
        
        heapq.heappush(heap_queue, [start_time, int(duration), subject])
        
    heapq.heappush(heap_queue, [float('inf'), float('inf'), float('inf')])
        
    st, dur, sub = heapq.heappop(heap_queue)
    cur_task = [st, dur, sub]
    stop_task = deque([])
    answer = []
    
    while heap_queue:
        c_st, c_dur, c_sub = cur_task
        st, dur, sub = heapq.heappop(heap_queue)
        
        if c_st + c_dur == st:
            cur_task = [st, dur, sub]
            answer.append(c_sub)
            
        elif c_st + c_dur < st:
            remain_time = st - c_st - c_dur
            answer.append(c_sub)
            
            while stop_task:
                s_st, s_dur, s_sub = stop_task.pop()
                if s_dur == remain_time:
                    answer.append(s_sub)
                    break
                elif s_dur < remain_time:
                    remain_time -= s_dur
                    answer.append(s_sub)
                else:
                    s_dur -= remain_time
                    stop_task.append([s_st, s_dur, s_sub])
                    break
            
            cur_task = [st, dur, sub]
            
        else:
            r_dur = c_dur - (st - c_st)
            stop_task.append([c_st, r_dur, c_sub])
            cur_task = [st, dur, sub]
        
    return answer

# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
# # ["korean", "english", "math"]
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# ["science", "history", "computer", "music"]
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
# # ["bbb", "ccc", "aaa"]


# 테스트 1 〉	통과 (0.03ms, 10.5MB)
# 테스트 2 〉	통과 (0.06ms, 10.5MB)
# 테스트 3 〉	통과 (0.09ms, 10.5MB)
# 테스트 4 〉	통과 (0.15ms, 10.4MB)
# 테스트 5 〉	통과 (0.11ms, 10.4MB)
# 테스트 6 〉	통과 (0.15ms, 10.6MB)
# 테스트 7 〉	통과 (0.17ms, 10.5MB)
# 테스트 8 〉	통과 (0.14ms, 10.4MB)
# 테스트 9 〉	통과 (0.36ms, 10.3MB)
# 테스트 10 〉	통과 (0.43ms, 10.5MB)
# 테스트 11 〉	통과 (0.61ms, 10.5MB)
# 테스트 12 〉	통과 (1.87ms, 10.6MB)
# 테스트 13 〉	통과 (1.90ms, 10.7MB)
# 테스트 14 〉	통과 (2.34ms, 10.7MB)
# 테스트 15 〉	통과 (2.31ms, 10.8MB)
# 테스트 16 〉	통과 (0.04ms, 10.5MB)
# 테스트 17 〉	통과 (0.04ms, 10.4MB)
# 테스트 18 〉	통과 (0.04ms, 10.5MB)
# 테스트 19 〉	통과 (0.05ms, 10.6MB)
# 테스트 20 〉	통과 (0.23ms, 10.5MB)
# 테스트 21 〉	통과 (0.38ms, 10.5MB)
# 테스트 22 〉	통과 (12.83ms, 10.7MB)
# 테스트 23 〉	통과 (2.61ms, 10.6MB)
# 테스트 24 〉	통과 (2.50ms, 10.6MB)