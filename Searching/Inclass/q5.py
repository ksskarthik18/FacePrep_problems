n = int(input())
nums = list(map(int,input().split()))
target = int(input())

def binarySearch(n,nums,target):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            low = mid
            return low
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(binarySearch(n,nums,target))