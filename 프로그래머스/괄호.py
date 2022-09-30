def solution(s):
    ck = []
    for i in s:
        if i=='(' or i=='{' or i=='[':
            ck.append(i)
        else:
            if not ck:
                return False
            x = ck.pop()
            if i == ')' and x != '(':
                return False
            elif i == ']' and x != '[':
                return False
            elif i == '}' and x != '{':
                return False
    return len(ck) == 0