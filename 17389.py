n = int(input())
lst = input()

total = 0
cnt = 0
for i in range(len(lst)):
    if lst[i] == 'O':
        total += (i+1)
        total += cnt
        cnt +=1

    else:
        cnt = 0

print(total)

