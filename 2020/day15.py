import io
import re
import sys
import time
from copy import deepcopy 

import aoc

# inputStr = '0,3,6'
inputStr = '18,8,0,5,4,1,20'
input = [int(v) for v in inputStr.split(',')]
print( str(input) )

def GetLastIndex( list, item ): 
    cnt = len(list)
    idx = cnt - 1
    while (idx >= 0): 
        idx -= 1
        if (list[idx] == item): 
            return idx 

    return -1 

total = 30000000
seen = dict()
for i in range(len(input) - 1): 
    seen[input[i]] = i 

lastInput = input[-1]
for i in range(len(input), total): 
    newVal = 0
    if lastInput in seen: 
        lastIdx = seen[lastInput]
        newVal = i - lastIdx - 1
    else: 
        newVal = 0

    seen[lastInput] = i - 1
    lastInput = newVal 

    if i % 100000 == 0: 
        print( 'step ' + str(i) )

print( lastInput )