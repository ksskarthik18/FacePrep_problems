nums = list(map(int,input().split()))
k = int(input())
def right_rotate(nums,k):
    l = len(nums)
    rem = l - k
    part1 = nums[:rem][::-1]
    part2 = nums[rem:][::-1]
    final = part1 + part2
    final = final[::-1]
    return final
result = right_rotate(nums,k)
print(*result)