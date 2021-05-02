def solution(n, lost, reserve):
    # 초기 answer = 전체 학생 수 - 도난당한 학생 수
    answer = n - len(lost)
    for i in lost:
        # 여분이 있는경우
        if i in reserve:
            continue
        # 도난당한 학생 i는 여분이 있는 i+1 또는 i-1 에게서 체육복을 받되
        # i+1 또는 i-1는 도난당한 학생(lost)에 해당되지 않을 경우에만 빌려줄 수 있음
        if (i+1) in reserve and (i+1) not in lost:
            reserve.remove(i+1) # 빌려줬으면 reserve에서 제거
            answer += 1         # 받았으니 체육수업 참가 가능
            continue
        elif (i-1) in reserve and (i-1) not in lost:
            reserve.remove(i-1)
            answer += 1
            continue
    # 도난당한 학생 중 여분이 있는 학생은 참가 가능
    for i in lost:
        if i in reserve:
            answer += 1
    return answer
