from collections import Counter
import itertools

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

lst = []
for k in course:
    lst_1 = []
    for i in orders:
        if len(i)>=k:
            for j in itertools.combinations(i,k):
                lst_1.append(tuple(sorted(j)))

    if lst_1:
        maxi = max(Counter(lst_1).values())
        if maxi > 1:
            for x,y in Counter(lst_1).items():
                if y == maxi:
                    word = ''
                    for zz in x:
                        word+=zz
                    lst.append(word)
print(sorted(lst))