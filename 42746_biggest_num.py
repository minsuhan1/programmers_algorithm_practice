def solution(numbers):
    tmp = []
    for n in numbers:
        n = str(n)
        tmp.append([n, n * (12 // len(n))])
    tmp.sort(key=lambda x:x[1], reverse=True)
    '''
    ex) numbers = [12, 121, 31]
        tmp = [[12, 121212121212], [121, 121121121121], [31, 313131313131]]
        tmp.sort -> tmp = [[31, 313131313131], [12, 121212121212], [121, 121121121121]]
        ans = [31, 12, 121]
    '''
    ans = ''
    for i in tmp:
        ans += i[0]

    return str(int(ans))
