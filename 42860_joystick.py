def solution(name):
    # 처리해야 하는 문자들 중
    # 현재 위치에서 가장 가까이 위치한 문자를 선택하여 처리
    # 커서 이동, 알파벳 변경 시 빠른 방법을 선택
    answer = 0
    cursor = 0    # 커서의 초기 위치
    target = []
    # 처리해야 하는 문자 위치를 target에 저장
    for i in range(len(name)):
        if name[i] != "A":  target.append(i)
    while(len(target)):
        # diff: target들 각각의 커서와의 위치 차이(위치 차이는 커서이동이 적은 방법을 선택)
        diff = list(map(lambda x: min(abs(cursor - x), len(name) - abs(cursor - x)), target)) 
        loc = target[diff.index(min(diff))] # target중 커서와 가장 가까이 있는 target 위치
        answer += min(diff)
        # 해당 위치의 알파벳을 만들기 위해 버튼 누르는 횟수 선택
        cursor = loc
        answer += min(ord(name[loc]) - ord("A"), 26 - (ord(name[loc]) - ord("A")))
        # 처리된 target 위치 제거
        target.remove(loc)

    return answer
