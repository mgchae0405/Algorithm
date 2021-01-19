def solution(skill, skill_trees):
    cnt = 0
    for thing in skill_trees:
        idx =0
        ck = True
        total = 0

        for i in range(len(thing)):
            if thing[i] not in skill:
                total +=1

            elif thing[i] != skill[idx]:
                break
            else:
                idx+=1
                if idx == len(skill):
                    cnt+=1
                    print('else',thing,i)
                    break
            if i == (len(thing) - 1) and idx != 0:
                print(thing, i)
                cnt += 1
                break

        if total == len(thing):
            cnt+=1
    return cnt