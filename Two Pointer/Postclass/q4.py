n = int(input())
nums = list(map(int,input().split()))

def findLongestMountain(n,nums):
    i = 1
    longest = 0
    while i < n -1:
        if nums[i-1]<nums[i] and nums[i] > nums[i+1]:
            left = i -1
            right = i + 1
            while left > 0 and nums[left-1] < nums[left]:
                left -=1
            while right < n - 1 and nums[right] > nums[right+1]:
                right += 1
            longest = max(longest,right-left+1)
            i = right
        else:
            i+=1
    return longest

print(findLongestMountain(n,nums))


