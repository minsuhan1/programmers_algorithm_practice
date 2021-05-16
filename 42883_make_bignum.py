def solution(number, k):
    answer = ''
    stack = []
    n = 0
    # 순서대로 스택에 넣다가
    # 큰 수를 만나면 해당 수보다 작은 수들을 스택에서 꺼낸다
    # 제거횟수가 제거할 수 k에 도달할 때까지
    for i in number:
        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)
    # 제거가 덜 된 경우 뒤에서 빼낸다(ex. "121", k = 2)
    if k > 0:
        for _ in range(k):
            stack.pop()
    
    answer = "".join(stack)
    return answer
