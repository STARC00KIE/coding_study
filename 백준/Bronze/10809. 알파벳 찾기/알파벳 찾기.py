word = list(input())
alphabet = list('abcdefghijklmnopqrstuvwxyz')

for i in range(len(alphabet)):
    for j in range(len(word)):
        if alphabet[i] == word[j]:
            print(f"{j}", end=' ')
            break
        elif (j+1) == len(word):
            print("-1", end=' ')