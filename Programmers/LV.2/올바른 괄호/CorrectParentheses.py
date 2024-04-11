'''
입력받은 문자열을 분리하여 저장한다
(인 경우 +1
)인 경우 -1을 하고
도중 값이 음수가 되면 F -> (())), )
모두 확인 후 값이 0이 아니면 F -> ((())
'''


def solution(s):
    answer = True
    count = 0
    list(s)
    for check in s:
        if check == '(':
            count += 1
        elif check == ')':
            count -= 1
            if count < 0:
                answer = False
                break
    if count != 0:
        answer = False
    return answer


print(solution("()      ())) ()"))
