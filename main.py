def f_1624(x, y, z, w):
    return ((x <= y) and (y <= w)) or (z == (x or y))


def pol_1624():
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                for w in range(0, 2):
                    if f_1624(x, y, z, w) == 0:
                        print(x, y, z, w)


def f_1619(x, y, z):
    return int((x <= (not z)) and (y or x))


print('x y z   f')
print('----------')


def pol_1619():
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(x, y, z, ' ', f_1619(x, y, z))


def f_1628(x, y, z, w):
    return (x and z) or ((w <= x) == (z <= y))


def pol_1628():
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                for w in range(0, 2):
                    if f_1628(x, y, z, w) == 0:
                        print(x, y, z, w)

pol_1628()
