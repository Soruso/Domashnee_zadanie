from functools import wraps


def val_checker(func_filter):

    def checker(func):

        @wraps(func)
        def decor(x):

            if func_filter(x):
                return func(x)

            raise ValueError from ValueError

        return decor

    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

deco = input()
deco = int(deco)
print(calc_cube(deco))
