'''
생각 흐름

리스트 index 사용해서 위치 반환
'''

def solution(seoul):

    position = seoul.index('Kim')
    answer = "김서방은 " +str(position) +"에 있다"
    return answer