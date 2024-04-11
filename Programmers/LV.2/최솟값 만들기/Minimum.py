'''
배열 1을 오름차순으로
배열 2를 내림차순으로 정렬하고
배열 1의 값과 배열 2의 값을 곱하면
최솟값이 나온다.
zip 함수 -> 여러 개의 순회 가능한(iterable) 객체를 인자로 받고,
각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환
'''


def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i, x in zip(A, B):
        answer += i * x

    return answer

