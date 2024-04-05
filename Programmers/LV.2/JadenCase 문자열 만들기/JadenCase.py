'''
공백 다음의 알파벳인지 알기 위해 check 변수를 사용
check = False이면 단어의 첫 알파벳 -> 대문자면 그대로, 소문자면 대문자로 바꿈
check = True이면 첫 알파벳이 아님 -> 대문자면 소문자로 바꾼다, 소문자면 그대로
공백이면 False로 바꾸어 다음 알파벳이 처음임을 알림
공백과 알파벳이 아닌경우 True로 설정해 다음 알파벳이 있음을 알려줌

+ 모두 소문자로 바꾸고 하면 더 편할듯
'''


def solution(s):
    answer = ''
    s = list(s)
    check = False
    for index, value in enumerate(s):
        if value.isupper() and check == False:
            check = True
        elif value.isupper() and check:
            s[index] = value.lower()
        elif value.islower() and check == False:
            s[index] = value.upper()
            check = True
        elif value.islower() and check:
            continue
        elif value == " ":
            check = False
        else:
            check = True

    answer = ''.join(s)

    return answer

