src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def f1():
    x = None
    result = []
    for i in src:
        if x and i > x:
            result.append(i)
        x = i
    return result

new_list = f1()
print(new_list)
