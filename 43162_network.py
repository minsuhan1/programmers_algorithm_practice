def solution(n, computers):
    visited = [0] * n    
    answer = 0
    def dfs(node):
        visited[node] = 1	# 방문처리
        for i in range(n):
        	# 방문하지 않은 정점이고, node와 연결되어 있는 i 정점에 대해 dfs
            if visited[i] == 0 and computers[node][i] == 1:
                dfs(i)
        return 1
	
    # 방문하지 않은 정점들에 대해 DFS 수행
    for i in range(n):
        if visited[i] == 0:
            answer += dfs(i)
    return answer
