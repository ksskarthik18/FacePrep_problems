sentence = input()
sentence = sentence.split(" ")
for i in sentence:
    print(i[::-1],end = " ")