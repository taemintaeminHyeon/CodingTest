'''
입력 받은 수(n) 만큼 n번째 뒤의 알파벳으로 변경되어야 하기 때문에
아스키 코드로 변경하여 계산한다.
이때 마지막 문자인 z,Z 인 경우 다시 a,A 로 돌아가야하므로
여기서는 -26을 해줘 해당 문자로 돌아가도록 설정하였다.

나머지 아스키 코드는 변경할 필요가 없으므로
answer에 추가하여
최종 문자열 answer을 리턴함

'''

def solution(s, n):
    answer = ''

    alphabets = list(s)
    print(alphabets)

    for alphabet in alphabets:

        if ord(alphabet) > 122:
            answer += str(alphabet)
            continue
        elif ord(alphabet) > 96:
            if ord(alphabet)+n > 122:
                answer += chr(ord(alphabet)+n-26)
                continue

            answer += chr(ord(alphabet)+n)
        elif ord(alphabet) > 90:
            continue
        elif ord(alphabet) > 64:
            if ord(alphabet) + n > 90:
                answer += chr(ord(alphabet) + n - 26)
                continue

            answer += chr(ord(alphabet) + n)
        else:
            answer += str(alphabet)
            continue


    return answer

print(solution("a B z", 4))