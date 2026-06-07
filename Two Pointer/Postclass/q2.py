n = int(input())
nums = list(map(int,input().split()))
def findSquares(n,nums):
    left = 0
    right = n -1
    ans =[0]*n
    pos = n - 1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            ans[pos] = abs(nums[left]) * abs(nums[left])
            left+=1
        else:
            ans[pos] = abs(nums[right]*abs(nums[right]))
            right-=1
        pos-=1
    print(*ans)
findSquares(n,nums)