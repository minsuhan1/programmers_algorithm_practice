from itertools import permutations

# 소수판별함수
def isprime(num):
    if num <= 1: return False
    if num == 2: return True
    for i in range(2, int(num ** (1/2))+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    # input 문자열 분할
    numbers = [numbers[i] for i in range(len(numbers))]
    # 조각을 붙여 만들 수 있는 모든 수 생성
    permute = []
    answer = []
    for i in range(1, len(numbers)+1):
        permute = permute + list("".join(_) for _ in permutations(numbers, i))
    # 숫자로 바꾸고 중복제거
    permute = list(set(map(int, permute)))
    # 소수만 answer에 저장
    for i in permute:
        if isprime(i) == True:
            answer.append(i)
    return len(answer)
