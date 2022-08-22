from collections import Counter


lst = list(map(int, input().split(' ')))

if len(set(lst)) == 1:
    print((lst[0] * 1000) +10000)
elif len(set(lst)) == 2:
    print(1000+(sorted(Counter(lst).items(), key=lambda x: x[1], reverse=True)[0][0])*100)
else:
    print(max(lst)*100)