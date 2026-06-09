n = int(input())
nums = list(map(int,input().split()))
target = int(input())

low = 0
high = n - 1
while low <= high:
    mid = (low + high)//2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid]<target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(low)