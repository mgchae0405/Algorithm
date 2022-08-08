T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split(' ')))
    for i in range(len(lst)):
        if lst[i]%2 !=0:
            lst[i]+=1

    cnt = 0
    while True:
        if len(set(lst)) == 1:
            break
        lst2 = [0 for _ in range(len(lst))]
        for i in range(len(lst)-1):
            lst2[i+1] = (lst[i]/2)+(lst[i+1]/2)
        lst2[0] = (lst[-1]/2)+(lst[0]/2)

        lst = [ i if i % 2 == 0 else i+1 for i in lst2 ]

        cnt+=1
    print(cnt)