k1, b1 = map(int, input().split())
k2, b2 = map(int, input().split())
if k1 == k2:
    if b1 == b2:
        print('coincide')
    else:
        print('parallel')
elif b1 == b2:
    print('intersect')
    print(0, b1)
else:
    print('intersect')
    x = (b2 - b1)/(k1 - k2)
    y = k1 * x + b1
    print(x, y)
