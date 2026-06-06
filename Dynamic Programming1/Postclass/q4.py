n , maxweight = map(int,input().split())
weights = list(map(int,input().split()))
values = list(map(int,input().split()))

dp = [[0]*(maxweight+1) for _ in range(n+1)]

for i in range(1,n+1):
    for w in range(1,maxweight+1):
        if weights[i-1] <= w:
            dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]])
        else:
            dp[i][w] = dp[i-1][w]
print(dp[n][maxweight])