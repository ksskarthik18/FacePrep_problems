m , n = map(int,input().split())
matrix = []
for _ in range(m):
    matrix.append(list(map(int,input().split())))
target = int(input())
low = 0
high = m * n - 1
while low <= high:
    mid = (low+high)//2
    row = mid//n
    col = mid%n
    if matrix[row][col] == target:
        print("true")
        break
    elif matrix[row][col] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("false")