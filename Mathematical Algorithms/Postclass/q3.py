import math
start , end = map(int,input().split())
count = 0
for i in range(start,end+1):
    root = math.isqrt(i)
    if root * root == i:
        count+=1
print(count)
