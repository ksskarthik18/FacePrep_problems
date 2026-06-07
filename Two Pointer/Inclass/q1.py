def reverse_str_slicing(s,k):
    chars = list(s)
    for i in range(0,len(s),2*k):
        chars[i:i+k] = reversed(chars[i:i+k])
    return "".join(chars)



s = input()
k = int(input())
print(reverse_str_slicing(s,k))
