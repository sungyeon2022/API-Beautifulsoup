def solution(text, anagram, sw):
    answer = ['']*len(text)
    if sw:
        for i in range(len(answer)):
            answer[anagram[i]]=text[i]
    else:
        for i in range(len(answer)):
            answer[i]=text[anagram[i]]
    print(''.join(answer))
    return ''.join(answer)

solution("hello",[4,2,0,1,3],False)
