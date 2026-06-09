n = int(input())
low = 0
high = int(n**0.5)

while low<=high:
    s = (low*low) + (high*high)
    if s == n:
        print("true")
        break
    elif s < n:
        low += 1
    else:
        high -= 1
else:
    print("false")
