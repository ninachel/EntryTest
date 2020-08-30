k = int(input())
side = k / 4 + 1
if k == 1:
    print('YES')
elif (side**2).is_integer():
    print('YES')
else:
    print('NO')
