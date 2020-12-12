import io
import re
import sys
import time
from copy import deepcopy 

import aoc


# config
INPUT_FILE = 'day12.input.txt';
REMOVE_LINE_BREAKS = True

# read input
input = aoc.ImportInput(INPUT_FILE, REMOVE_LINE_BREAKS)

# implementation
dirs = []
for idx, line in enumerate(input): 
    dirs.append( [line[0], int(line[1:])] )
    # print( str(dirs[idx]) )

def Turn( dx, dy, dir ): 
    turns = int(dir / 90)
    d = [dx, dy]
    while (turns >= 4): 
        turns -= 4
    while (turns < 0): 
        turns += 4

    if (turns == 0): 
        return dx, dy
    elif (turns == 1): 
        return dy, -dx
    elif (turns == 2):
        return -dx, -dy
    elif (turns == 3): 
        return -dy, dx
#end Turn


def Part01():
    x = 0
    y = 0
    dx = 1
    dy = 0

    for dir in dirs: 
        com = dir[0]
        val = dir[1]
        # print( '{}: {}'.format( com, val ) )

        if (com == 'N'): 
            y += val 
        elif (com == 'S'): 
            y -= val
        elif (com == 'E'):
            x += val
        elif (com == 'W'): 
            x -= val 
        elif (com == 'F'): 
            x += dx * val
            y += dy * val
        elif (com == 'L'): 
            dx, dy = Turn( dx, dy, -val )
        elif (com == 'R'): 
            dx, dy = Turn( dx, dy, val )

        # print( 'Location: {}, {}'.format( x, y ) )
    #end for

    dist = abs(x) + abs(y)
    print( 'Part01 dist traveled: {}'.format(dist) )
#endif Part01

def Part02():
    x = 0
    y = 0
    wx = 10
    wy = 1

    # so if i rotate the ship, I rotate the waypoint.
    # ship's direction doesn't actually matter - isn't used for anyting

    for dir in dirs: 
        com = dir[0]
        val = dir[1]

        if (com == 'N'): 
            wy += val 
        elif (com == 'S'): 
            wy -= val
        elif (com == 'E'):
            wx += val
        elif (com == 'W'): 
            wx -= val 
        elif (com == 'F'): 
            x += wx * val
            y += wy * val
        elif (com == 'L'): 
            wx, wy = Turn( wx, wy, -val )
        elif (com == 'R'): 
            wx, wy = Turn( wx, wy, val )

        # print( 'Location: {}, {}'.format( x, y ) )
    #end for

    dist = abs(x) + abs(y)
    print( 'Part02 dist traveled: {}'.format(dist) )
#endif Part01
        
# print( str( Turn( 1, 0, -270 ) ) )

progStart = time.time()

part01Time = time.time()
Part01()
print( 'Part01 took: {:.4f}ms'.format( (time.time() - part01Time) * 1000.0 ) )

print()
part02Time = time.time()
Part02()
print( 'Part02 took: {:.4f}ms'.format( (time.time() - part02Time) * 1000.0 ) )

print( '\nTotal time: {:.4f}ms'.format( (time.time() - progStart) * 1000.0 ) )
