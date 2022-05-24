def get_digits_sum(x):
    result = 0
    while x != 0:
        result += x % 10
        x = x // 10
    return result
def solution_1():
    sum = 0
    cube = 0
    for i in range(1,1000,2):
        cube = i ** 3
        if get_digits_sum(cube) % 7 == 0:
            sum += cube
    print(sum)
def solution_2():
    sum = 0
    cube = 0
    for i in range(1,1000,2):
        cube = i ** 3 + 17
        if get_digits_sum(cube) % 7 == 0:
            sum += cube
    print(sum)

solution_1()
solution_2()