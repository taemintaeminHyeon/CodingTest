'''
생각 흐름

해당 문자의 앞 부분만 확인하면 되기 때문에
enumerate를 이용하여 인덱스를 함께 가져와
해당 부분까지만 슬라이싱하여 비교한다
같은 문자가 있는 경우 해당 위치를 저장하고
반복하여 최종적으로 마지막 중복 문자의 위치를 카운트하고
자신의 위치에서 저장된 위치를 빼서 문자간 사이를 리턴한다.

중복된 문자가 없는 경우는 -1을 리턴한다.
'''

def solution(s):
    answer = []

    for index, letter in enumerate(s):
        count = -1
        for i in range(0, index):

            if s[i] == letter:
                count = i

        if count > -1:
            answer.append(index - count)
            continue

        answer.append(-1)


    return answer



'''

반복문 하나 없이도 가능하다.
이러면 시간 복잡도가 더 줄어든다.
'''
def solution2(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer

