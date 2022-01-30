N = int(input())
order = input().split()
row = 1
col = 1


for o in order:
    if o == 'L':
        col = col - 1
        if col <= 0:
            col = 1

    elif o == 'R':
        col = col + 1
        if col > N:
            col = N

    elif o == 'U':
        row = row - 1
        if row <= 0:
            row = 1

    elif o == 'D':
        row = row + 1
        if row > N:
            row = N

print('{} {}'.format(row, col))