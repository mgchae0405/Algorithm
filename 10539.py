n = int(input())
lst = list(map(int, input().split()))

for i in range(1, len(lst)):
    lst[i] = lst[i]*(i+1) - sum(lst[:i])

for k in lst:
    print(k, end=' ')
