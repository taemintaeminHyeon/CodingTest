'''
commands의 구성은 똑같기 때문에
직접 숫자를 넣어서 구성함

이후 슬라이싱을 이용해
원하는 구간만큼 슬라이싱 한 후
sort 함수를 이용해 오름차순으로 정렬한다.

이후 해당 인덱스의 요소를 반환하여
answer 리스트에 추가하여 최종 answer을 반환한다.

주의 : 매개변수로 들어온 값을 덮어쓰지 말자!
'''

def solution(array, commands):
    answer = []


    for i in commands:
        firstIndex = i[0] - 1
        secondeIndex = i[1]
        numberIndex = i[2] - 1

        sortArray = sorted(array[firstIndex:secondeIndex])
        answer.append(sortArray[numberIndex])

    return answer
