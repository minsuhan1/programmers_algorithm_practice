def solution(begin, target, words):
    answer = 0
    # target이 words 안에 없는 경우 0 리턴
    if target not in words:
        return 0;
    # BFS로 현재 단어에서 한 문자만 바꿔서 변환할 수 있는 단어들을 탐색
    # 해당 단어들은 현재 단어 depth + 1 을 depth로 가짐
    # 만약 해당 단어들 중 target이 존재하면 depth를 바로 리턴 
    queue = []
    queue.append((begin, 0))
    while queue:
        now, depth = queue.pop(0)
        for w in words:
            diff = 0
            for i in range(len(w)):
                if now[i] != w[i]:  diff += 1
            if (diff == 1) and (w == target):
                depth += 1
                return depth
            elif diff == 1:
                queue.append((w, depth+1))
    return answer
