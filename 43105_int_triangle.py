def solution(triangle):
    height = len(triangle)
    dp = [[0] * i for i in range(1, height+1)]
    answer = 0
    for i in range(height):
        for j in range(len(dp[i])):
            # 첫 줄
            if i == 0 and j == 0:   
                dp[i][j] = triangle[i][j]
                continue
            # 각 줄의 양 끝
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]   # 오른쪽 위 dp + 현재값
                continue
            if j == len(dp[i])-1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]    # 왼쪽 위 dp + 현재값
                continue
            # 왼쪽 위 dp, 오른쪽 위 dp 중 큰 값에 현재값을 더함
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    answer = max(dp[height-1])
    return answer
