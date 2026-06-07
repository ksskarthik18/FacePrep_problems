def isPalindrome(str1):
    left= 0
    right = len(str1)-1

    while left < right:
        while left < right and not str1[left].isalnum():
            left+=1
        while left < right and not str1[right].isalnum():
            right-=1
        
        if str1[left].lower() != str1[right].lower():
            return "false"
        else:
            left+=1
            right-=1
    return "true"
str1 = input()
print(isPalindrome(str1))