info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

info_lst = [i.split(' ') for i in info]
print(info_lst)
print('-----------------------------')

query_lst =[[k for k in j.split(' ') if k != 'and'] for j in query]
print(query_lst)
#print('---------------------------------')
lst= []
for i in query_lst:
    cnt =0
    for j in info_lst:
        for cc in range(4):
            if i[cc]!='-' and i[cc] != j[cc]:
                break
            # elif i[cc] == j[cc]:
            # else:
            #     break
            if cc==3:
                if int(j[4])>=int(i[4]):
                    cnt+=1
    lst.append(cnt)

print(lst)