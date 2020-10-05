def bitmasks(n,m):
    if m < n:
        if m > 0:
            for x in bitmasks(n-1,m-1):
                yield (1 << (n-1)) + x
            for x in bitmasks(n-1,m):
                yield x
        else:
            yield 0
    else:
        yield (1 << n) - 1

if __name__ == '__main__':
    for b in bitmasks(3,2):
        print(b)
