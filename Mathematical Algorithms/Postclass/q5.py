n = input()
for i in range(len(n)-1):
    if abs(int(n[i]) - int(n[i+1])) > 1:
        print("Not Jumbled")
        break

else:
    print("Jumbled")