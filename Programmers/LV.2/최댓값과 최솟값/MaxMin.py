'''
공백을 기준으로 분리하여
오름차순으로 정렬한다, 이때 숫자들이 문자열로 인식이 되므로
(문자열일 경우 -1, -2 비교시 -를 비교한 후 1,2를 비교한다)
int로 변경하여 정렬한다

map(function, iterable) 함수 => iterable의 각 요소에 대해 function 함수를 적용한 결과를 새로운 iterator로 반환
'''


def solution(s):
    s = list(map(int, s.split()))
    s.sort()
    answer = str(s[0]) + " " + str(s[-1])
    return answer

