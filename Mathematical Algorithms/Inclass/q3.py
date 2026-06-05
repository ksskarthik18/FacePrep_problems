num = int(input())
def findDivisors(num):
    for i in range(1,num+1):
        if num % i == 0:
            print(i,end = " ")

findDivisors(num)