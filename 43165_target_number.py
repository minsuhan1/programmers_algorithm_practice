def solution(numbers, target):
    answer = 0
    len_n = len(numbers)
    def dfs(idx = 0):
        if idx < len_n:
            numbers[idx] *= -1
            dfs(idx+1)

            numbers[idx] *= -1
            dfs(idx+1)
        elif sum(numbers) == target:
            nonlocal answer
            answer += 1

    dfs();
    return answer
