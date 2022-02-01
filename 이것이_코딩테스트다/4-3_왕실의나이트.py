loc = input()
col = loc[0]
row = loc[1]

count = 0
while True:
    if col >= 'c' or col <= 'f':
        if int(row) >= 2 or int(row) <= 2:
            count += 1
        else:
            break