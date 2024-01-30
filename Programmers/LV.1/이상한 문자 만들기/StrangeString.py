'''
생각 흐름

공백 기준으로 split하여
각 단어를 기준으로
짝수면 대문자, 홀수면 소문자로 변환하여
공백을 포함하여 연결한다.

여기서
split(), split(" ") 는 다르다!
'''

def solution(s):
    answer = ''
    words = s.split(" ") # 공백을 기준으로 분리함

    for i, word in enumerate(words):
        alphabets = list(word)
        for index, alphabet in enumerate(alphabets):
            if index % 2 == 0:
                alphabets[index] = alphabet.upper()
            else:
                alphabets[index] = alphabet.lower()

        words[i] = "".join(alphabets)


    print(words)
    answer=" ".join(words)






    return answer

