import numpy as np
from operator import itemgetter
from itertools import groupby

with open("Snakesdata.txt") as f:
    content = f.readlines()

T = int(content[0])
tnext = 0

for t in range(T):
    
    N = int(content[1 + tnext])
    M = int(content[2 + N + tnext])

    ladder = np.empty([N , 2] , dtype=int)
    snake = np.empty([M , 2] , dtype=int)

    for j in range(2 + tnext , 2 + tnext + N):
        ladder[j - 2 - tnext][0] = int( content[j].split()[0] )
        ladder[j - 2 - tnext][1] =  int( content[j].split()[1] )
    for j in range(3 + N + tnext , 3 + tnext + N + M):
        snake[j - 3 - tnext - N][0] = int( content[j].split()[0] )
        snake[j - 3 - tnext - N][1] =  int( content[j].split()[1] )

    data = snake[:,0]
    length = 0
    for k, g in groupby(enumerate(data), lambda ix: ix[0] - ix[1]):
        length = max(length, len( list(map(itemgetter(1), g)) ))
    if length >= 6:
        print(-1)
        break
    # if there are 6 snakes in a row

    minsquare = [1000]*101
    minsquare[1]=0
    i=2
    while i <= 100:
        if i not in ladder[:,0]:
            if i in ladder[:,1]:
                index = int(np.where(ladder == i)[0]) # np.where gives the idices of value i
                start = ladder[index, 0]
                for j in range(1, min(7, start ) ):
                    minsquare[i] = min(minsquare[start -j]+1, minsquare[i])
            for j in range(1, min(7, i) ):
                minsquare[i] = min(minsquare[i-j]+1, minsquare[i])
            if i in snake[:,0]:
                index = int(np.where(snake == i)[0])
                tail = snake[index, 1]
                if minsquare[tail] > minsquare[i]:
                    minsquare[tail] = minsquare[i]
                    i = tail
                minsquare[i] = 1000
        i += 1

    print(minsquare[100])
        
    tnext = N + M + 2 + tnext
