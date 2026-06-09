n = int(input())
nums = list(map(int,input().split()))
target = int(input())

def findIndexOfNum(n,nums,target):
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high-low)//2
        if nums[mid]== target:
            return mid
        elif nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            
            else:
                high = mid - 1
    return -1
print(findIndexOfNum(n,nums,target))