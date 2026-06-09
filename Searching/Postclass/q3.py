n = int(input())
nums = list(map(int,input().split()))
target = int(input())

low = 0
high = n - 1
while low <= high:
    mid = (low + high)//2
    if nums[mid] == target:
        print("true")
        break
    if nums[low] == nums[mid] == nums[high]:
        low += 1
        high -=1
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
else:
    print("false")