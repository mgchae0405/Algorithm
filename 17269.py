
n,m  = map(int, input().split())
a,b = input().split()

strr = ''
if len(a) >= len(b):
    for i in range(len(b)):
        strr += a[i]
        strr += b[i]
    strr += a[len(b):]
else:
    for i in range(len(a)):
        strr += a[i]
        strr += b[i]
    strr += b[len(a):]
strr = strr.lower()


dct = {'a':3, 'b':2, 'c':1, 'd':2, 'e':4, 'f':3, 'g':1, 'h':3, 'i':1, 'j':1, 'k':3, 'l':1, 'm':3, 'n':2, 'o':1, 'p':2, 'q':2, 'r':2, 's':1, 't':2, 'u':1, 'v':1, 'w':1, 'x':2, 'y':2, 'z':1}

strr2 = ''
for k in range(len(strr)-1):
    strr2 += str(dct[strr[k]] + dct[strr[k+1]])

cnt = 0
while len(str(strr2))>2:
    strr3 = ''
    for i in range(len(str(strr2))-1):
        strr3 += str(int(str(strr2)[i]) + int(str(strr2)[i+1]))[-1]
    strr2 = strr3

print(str(int(strr2)) + '%')