n = int(input())
nums = list(map(int,input().split()))
def gcd(a,b):
    while b:
        a , b = b ,a%b
    return a
ans = nums[0]
for i in range(n):
    ans = gcd(ans,nums[i])
print(ans)

