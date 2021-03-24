import sys

def Take_Input():
        
    lines, length = list(map(int, sys.stdin.readline().rstrip().split())) 
   
    grid = []
    for l in range(lines):
        grid.append(sys.stdin.readline().rstrip().lower())

    nwords = int(input())
    words = []
    for l in range(nwords):
        words.append(sys.stdin.readline().rstrip().lower())
        

    return grid, words


def find_word(grid, word):
    operations = ((1, 0), (-1, 0), (0, 1), (0, -1), 
            (1, 1), (-1, -1), (1, -1), (-1, 1))

    nlines = len(grid)
    ncolumns = len(grid[0])

    for l in range(0, nlines):
        for c in range(0, ncolumns):
            if grid[l][c] != word[0]:
                continue

            for op in operations:
                for letter in range(len(word)):
                    opc = c+op[0]*letter
                    opl = l+op[1]*letter

                    if opc<0 or opc>=ncolumns or opl<0 or opl>=nlines:
                        break
                    if grid[opl][opc] != word[letter]:
                        break
                else:
                    return (l, c)


def output(grid, words):
    return [find_word(grid, word) for word in words]


   
cases = int(input())
sys.stdin.readline()
for case in range(cases):
    positions = output(*Take_Input())
    print(" ")
    for line, column in positions:
        print(line+1, column+1)

    if case+1 < cases:
        print("")
