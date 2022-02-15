p = input()

q = p.replace('XXXX', 'AAAA')
result = q.replace('XX', 'BB')

if result.find('X') == -1:
    print(result)
else:
    print(-1)