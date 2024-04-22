'''
재귀함수 실패... (시간초과)
단순히 생각해서
0 1 -> 1
1 1 -> 2
1 2 -> 3
2 3 -> 5
3 5 -> 8
f(n) f(n+1) -> f(n+2) 를 구하면 된다


'''

def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a % 1234567
