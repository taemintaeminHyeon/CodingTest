'''
생각 흐름

맨 처음 값은 중복이 생길 수 없기 때문에
우선 리스트에 저장한 후
그 뒤의 값 부터 비교하여
값이 같으면 숫자가 연속이므로 answer에 저장하지 않고
다른 경우 연속이 아니므로 answer에 저장하여
연속적으로 나타나는 숫자를 제거 한 리스트를 반환한다.
'''


def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr[1:]:
        if answer[-1] != i:
            answer.append(i)


    return answer
