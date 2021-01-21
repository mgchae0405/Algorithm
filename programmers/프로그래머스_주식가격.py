prices = [1, 2, 3, 2, 3]
dp = [0]*len(prices)


for i in range(len(prices)):
    cnt = 0
    for j in range(i+1,len(prices)):
        if prices[i] <= prices[j]:
            dp[i]+=1
            print(dp)




print(dp)