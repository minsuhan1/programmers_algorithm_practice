def solution(n, times):
    answer = 0
    # n명의 사람들은 늦어도 n * min(times)분 안에는 모두 심사를 마칠 수 있다.
    # 따라서 심사하는 데 n * min(times)분보다 더 오래 걸리는 심사관에겐 갈 필요가 없다.
    max = n * min(times)
    times = list(filter(lambda x: x <= max, times))
    
    # 주어진 시간(minute) 안에 모든 사람들을 심사할 수 있는지 판별하는 함수
    # 각 심사관들이 minute 내에 최대로 심사 가능한 사람 수를 합하여
    # 합이 n보다 작으면 주어진 minute 내에 심사가 불가능함을 뜻한다.
    def isPossible(minute, n):
        sum = 0
        for i in times:
            sum += (minute // i)
        if sum < n: return False
        return True
    
    # 최단 시간을 이분탐색
    start = min(times)
    end = max
    while(start < end):
        mid = (start + end) // 2
        # mid분 내에 계산 가능하면 더 짧은 시간이 있는지 탐색
        # 불가능하면 더 긴 시간을 탐색
        if isPossible(mid, n):
            end = mid
        else:
            start = mid + 1
            
    # while 탈출 시점의 start(or end)값 = 최단시간
    answer = start
    return answer
