'''
n개를 가지고 있으며
a개를 주면 b만큼 주는 방식이므로
n에서 몇개를 줄지를 구한 다음
준 것으로 몇 개를 얻은지를 구하고
반복하여 n이 a보다 작아질 때 까지 반복하면
결과값이 나온다.

'''


def solution(a, b, n):
    answer = 0
    check = 0
    while n >= a:
        check = n//a
        n = n - check * a + b*check
        answer += b*check

    return answer
