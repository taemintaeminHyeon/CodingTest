'''
해당 인덱스에 속한 알파벳의 정렬에 따라
단어를 정렬해야 하며 알파벳이 똑같다면 단어의 오름차순 순서에 따라
정렬을 해야한다.

우선 단어를 먼저 정렬을 한다면 알파벳이 동일한 경우의 순서를 결정할 수 있다.

이후 해당 단어의 n번째 알파벳을 추출하여 정렬한 뒤

단어와 알파벳을 비교하여 똑같으면 answer에 추가해준다.
이때 맨 처음 알파벳은 answer에 추가되어 있을 것 이므로
answer에 들어간 경우 이것을 제외하고 추가해야한다
'''

def solution(strings, n):
    answer = []
    alphabets = []

    newStrings = sorted(strings)

    for s in newStrings:
        alphabets.append(s[n])

    alphabets = sorted(alphabets)

    for alphabet in alphabets:
        for string in newStrings:
            if string[n] == alphabet and string not in answer:
                answer.append(string)


    return answer
