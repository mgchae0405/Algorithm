n = int(input())
lst = set(map(int, input().split(' ')))
m = int(input())
lst2 = list(map(int, input().split(' ')))

for i in lst2:
    if i in lst:
        print(1)
    else:
        print(0)

##############################################
#다른 풀이

# N,A = int(input()), {i for i in map(int, input().split())}
# M = input()
#
# for i in list(map(int, input().split())):
#     print(A.get(i,0))
#