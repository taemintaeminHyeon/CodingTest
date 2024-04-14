'''
짝수면 수
홀수면 박
'''
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"

    return answer

print(solution(6))