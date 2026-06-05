n , k = map(int,input().split())
nums= list(map(int,input().split()))
from math import gcd
count = 0
def lcm(a,b):
    return a * b // gcd(a,b)
for i in range(n):
    curr_lcm = 1
    for j in range(i,n):
        curr_lcm = lcm(curr_lcm,nums[j])
        if curr_lcm == k:
            count+=1
        elif curr_lcm > k:
            break
print(count)


