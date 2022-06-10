def gen(n):
    result = 1
    while result <= n:
        yield result
        result += 2

x = int(input())

g = gen(x)
while True:
    print(next(g))
