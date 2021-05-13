def solution(N, number):
    answer = 0
    # dp[i] = 숫자 N을 i+1번 사용하여 만들 수 있는 숫자 set
    # 5, 55, 555, ..., 55555555 우선 추가
    dp = [set([int(str(N)*i)]) for i in range(1, 9)]
    for i in range(8):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j-1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 * op2)
                    dp[i].add(op1 - op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        if number in dp[i]: # 최솟값을 찾았을 때
            return i+1
            
    return -1     # 못 찾았을 때
