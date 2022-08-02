n = int(input())
lst = set(map(int, input().split(' ')))
m = int(input())
lst2 = list(map(int, input().split(' ')))

for i in lst2:
    if i in lst:
        print(1)
    else:
        print(0)

