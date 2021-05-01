def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a1, a2, a3 = 0, 0, 0
    for i in range(len(answers)):
        if p1[i % 5] == answers[i]: a1 += 1
        if p2[i % 8] == answers[i]: a2 += 1
        if p3[i % 10] == answers[i]: a3 += 1
            
    answer = []
    winner = max(a1, a2, a3)
    if(a1 == winner):
        answer.append(1)
    if(a2 == winner):
        answer.append(2)
    if(a3 == winner):
        answer.append(3)
    return answer
