s = input().strip()
def reverseVowels(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1
    while left < right:
        if chars[left].lower() not in "aeiou":
            left+=1
            continue
        if chars[right].lower() not in "aeiou":
            right -= 1
            continue
        chars[left],chars[right] = chars[right],chars[left]
        left+=1
        right-=1
    return "".join(chars)
print(reverseVowels(s))