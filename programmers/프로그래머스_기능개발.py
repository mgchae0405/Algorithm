import math

def solution(progresses, speeds):
    lst = [100 - i for i in progresses]
    lst_2 = [math.ceil(lst[i] / speeds[i]) for i in range(len(speeds))]

    ans = []
    cnt = 0
    for i in range(len(lst_2)):
        if lst_2[cnt] < lst_2[i]:
            ans.append(i - cnt)
            cnt = i
    ans.append(len(lst_2) - cnt)

    return ans