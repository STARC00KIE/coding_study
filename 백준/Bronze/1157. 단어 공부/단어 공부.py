word = input()
word = list(word.upper())
count = {}

for i in word:
    try: count[i] += 1
    except: count[i] = 1

result = [k for k,v in count.items() if max(count.values()) == v]
if len(result) >= 2:
    result = '?'
print(','.join(result))