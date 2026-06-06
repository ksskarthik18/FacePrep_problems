s = input().strip()
n = len(s)

i = 0
j = n -1
def dp(i,j):
    if i > j:
        return 0
    if i == j:
        return 1
    elif s[i] == s[j]:
        return 2 + dp(i+1,j-1)
    else:
        return max(dp(i+1,j),dp(i,j-1))
result = dp(i,j)
print(result)