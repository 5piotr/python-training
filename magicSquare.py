import time
import itertools

def magicSquareFinder(s):
    squares = []
    tiles = list(range(1, s*s + 1))
    perm = itertools.permutations(tiles)
    magic = ((tiles[0] + tiles[-1]) / 2) * s
    
    for square in list(perm):
        sums = []
        sum1 = 0
        for i in range(0, s*s, s):
            for j in range(s):
                sum1 += square[i + j]
            sums.append(sum1)
            sum1 = 0
        for i in range(s):
            for j in range(0, s*s, s):
                sum1 += square[i + j]
            sums.append(sum1)
            sum1 = 0
        for i in range(s):     
            sum1 += square[i * (s + 1)]
        sums.append(sum1)
        sum1 = 0
        for i in range(s):     
            sum1 += square[i * (s - 1) + (s - 1)]
        sums.append(sum1)
        sum1 = 0
        
        uSums = set(sums)
        if len(uSums) == 1:     
            squares.append(square)
            
    return squares

def print1square(squares):
    print('example:')
    if len(squares) == 0:
        print('nothing to print')
    else:
        square = squares[0]
        s = int(len(square) ** 0.5)
        line = ''
        print(' ' + '-' * (s + (s - 1) + 2) + ' ')
        for i in range(0, s*s, s):
            for j in range(s):
                line += str(square[i + j])
                line += ' '
            print('| ' + line + '|')
            line = ''
        print(' ' + '-' * (s + (s - 1) + 2) + ' ')

while True:
    try:
        size = int(input('magic square size: '))
        break
    except:
        print('giv me da int!')

start = time.time()

squares = magicSquareFinder(size)
print(len(squares), 'squares')
print1square(squares)

finish = time.time()
print(round((finish - start),2), 's')
