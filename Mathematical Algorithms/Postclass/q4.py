from math import gcd
n , m = map(int,input().split())
nums = list(map(int,input().split()))
numsDivide = list(map(int,input().split()))

g= numsDivide[0]
for x in numsDivide[1:]:
    g = gcd(g,x)
nums.sort()
for i,num in enumerate(nums):
    if g % num == 0:
        print(i)
        break
else:
    print(-1)