def solution(progresses, speeds):
    answer = []
    while(len(progresses) > 0):
        # 각각 해당하는 speed만큼 진도를 늘림
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        # 맨 앞 작업이 100%가 되면
        # 뒤의 이미 끝난(진도율 >= 100%) 기능들도 배포(remove)하고
        # 배포할 때 buf+=1
        # 맨 앞 작업이 다시 진도율 < 100%인 경우 buf 초기화
        buf = 0
        while(progresses[0] >= 100):
            buf += 1
            progresses.remove(progresses[0])
            speeds.remove(speeds[0])
            if(len(progresses) == 0):  break
        if buf > 0:
            answer.append(buf)
    return answer
