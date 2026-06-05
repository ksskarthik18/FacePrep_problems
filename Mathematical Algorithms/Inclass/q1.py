start ,end = map(int,input().split())

def findPrime(start,end):
    for i in range(start,end):
        if i<2:
            continue
        flag = False
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                flag= True
                break
        
        if not flag:
            print(i,end= " ")
findPrime(start,end)

