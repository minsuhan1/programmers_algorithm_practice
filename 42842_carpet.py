# 먼저 노란색 격자가 한 줄로 이루어져 있다고 가정했을 때
# 갈색 격자 개수가 맞춰지는지 확인하고
# 맞지 않는다면 노란색 격자 줄을 늘려가면서(한 줄당 격자개수는 1/2) 다시 계산해본다
def solution(brown, yellow):
    y_line = 1;
    while(1):
        if (4 + 2 * yellow/y_line + 2*y_line) == brown: # 갈색 격자 개수
            break
        y_line += 1
    
    answer = []
    answer += [int(yellow/y_line) + 2, y_line + 2]
    return answer
