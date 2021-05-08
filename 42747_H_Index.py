def solution(citations):
    # 인용 횟수를 기준으로 내림차순 정렬
    citations = sorted(citations, reverse = True)
    h_max = max(citations)  # 최대 인용횟수
    answer = 0
    # 인용횟수가 h번 일때
    # h번째 논문의 인용횟수가 h번 이상이면
    # 앞의 논문들은 모두 h번 이상 인용된 것이므로 H-Index
    for h in range(h_max):
        if h > len(citations):
            continue
        if citations[h-1] >= h:
            answer = h
    return answer
