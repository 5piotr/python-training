from collections import defaultdict

li = []
try:
    with open('input.txt', 'r') as file:
        for line in file:
            li.append(line.rstrip())
except:
    print('something went wrong with file opening :(')

n, m = map(int, li[0].split())

groupA = li[1 : n+1]
#print(len(groupA),groupA[-1])
groupB = li[n+1 :]
#print(len(groupB),groupB[0])

res = defaultdict(list)
for i in range(len(groupB)):
    if groupB[i] not in groupA:
        res[i].append(str(-1))
    else:
        for j in range(len(groupA)):
            if groupB[i] == groupA[j]:
                res[i].append(str(j + 1))


with open('output.txt', 'w') as file:
    for v in res.values():
        file.write(' '.join(v) + '\n')

