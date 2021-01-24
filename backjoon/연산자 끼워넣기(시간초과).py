import sys
import itertools
sys.stdin=open("input.txt", "rt")
calc = ['+','-','*','//']



n = int(input())
lst = list(map(int,input().split()))
cal_lst1 = list(map(int,input().split()))

cal_lst2 = []

for i in range(4):
    if cal_lst1[i] > 0:
        for _ in range(cal_lst1[i]):
            cal_lst2.append(calc[i])

mini = 2147000000
maxi = -2147000000


for z in itertools.permutations(cal_lst2, n-1):
    total = lst[0]
    for i in range(len(z)):
        if total<0 and z[i]=='//' and lst[i+1]>=0:
            total = -eval(str(abs(total))+z[i]+str(lst[i+1]))
        else:
            total = eval(str(total)+z[i]+str(lst[i+1]))
    if mini > total:
        mini = total
    if maxi < total:
        maxi = total

print(maxi)
print(mini)
# [1,2,3,4,5,6]
