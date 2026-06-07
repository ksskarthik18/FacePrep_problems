n = int(input())
nums = list(map(int,input().split()))
def find_water_trap(n,nums):
    left = 0
    right = n-1
    left_max = 0
    right_max = 0
    water = 0
    while left < right:
        if nums[left] < nums[right]:
            if nums[left] >= left_max:
                left_max = nums[left]
            else:
                water += left_max - nums[left]
            left+=1
        else:
            if nums[right] >= right_max:
                right_max = nums[right]
            else:
                water += right_max- nums[right]
            right -= 1
    return water
print(find_water_trap(n,nums))