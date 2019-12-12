'''
problem from hacker rank
'''

a = [2, 4]
b = [16, 32, 96]

'''
def getTotalX(a, b):
    count = []
    for i in range(a[-1], b[0] + 1):
        count1 = set()
        count2 = set()
        for j in a:
            if i % j == 0:
                count1.add(i)
        for k in b:
            if k % i == 0:
                count2.add(i)
        count3 = count1.intersection(count2)
        if len(count3) > 0:
            count.append(count3)
            
    ct = set.intersection(*count)
    print(count)

getTotalX(a, b)
'''

def getTotalX(a, b):
    zak = list(range(a[-1], b[0] + 1))
    
    list1 = []
    for i in a:
        se = set()
        for j in zak:
            if j % i == 0:
                se.add(j)
        list1.append(se)
    ct1 = set.intersection(*list1)

    list2 = []
    for i in b:
        se = set()
        for j in zak:
            if i % j == 0:
                se.add(j)
        list2.append(se)
    ct2 = set.intersection(*list2)

    ct = set.intersection(ct1, ct2)

    print(ct)

getTotalX(a, b)








    
