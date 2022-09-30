def solution(arr):
    ans = []
    for i in arr:
        if ans[-1:]==[i]:continue
        ans.append(i)

    print(ans)
    return ans

solution([1,1,3,3,0,1,1])