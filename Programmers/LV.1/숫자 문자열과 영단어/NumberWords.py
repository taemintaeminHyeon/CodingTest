'''
생각 흐름

영어가 들어오면 해당 숫자로 변경해야하므로
딕셔너리를 이용해 매핑하기로 함

영단어를 체크하기 위해 english 리스트를 만들면서 number 리스트도 함께만들어
dict 함수로 딕셔너리로 만듬

이후 반복문에서
숫자로 들어오면 answer에 더해주고

알파벳으로 들어온다면
dict과 비교하여 동일한 영단어가 있을 경우
해당 맵핑되는 숫자를 answer에 더한다.

문제에서 정수형 반환을 원하였으므로
마지막에 형변환해줌
'''

def solution(s):
    answer = ''
    number = ['0', '1', '2', '3',
                '4', '5', '6', '7',
                '8', '9']
    english = ['zero', 'one', 'two', 'three',
                  'four', 'five', 'six', 'seven',
                  'eight', 'nine']
    temp = ''

    englishNumber = dict(zip(english,number))



    for sentence in s:

        if sentence in number:
            answer += sentence
            temp = ''
            continue

        temp += sentence

        if temp in english:
            answer += englishNumber[temp]
            temp = ''


    return int(answer)


'''

파이썬 함수 중 replace()를 이용하면
손쉽게 바꿀 수 있다


'''
def solution2(s):
    num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3",
               "four": "4", "five": "5", "six": "6", "seven": "7",
               "eight": "8", "nine": "9"}

    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

print(solution("one4seveneight"))