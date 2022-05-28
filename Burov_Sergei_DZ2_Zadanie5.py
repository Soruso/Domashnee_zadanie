lst = [57.8, 46.51, 97, 23.56, 75.22, 90.01, 76.6, 37.80, 50.21, 1.90]
lst.sort()
def output():
    for i in lst:
        num = int(i)
        num_2 = i % 1 * 100
        num_2 = round(num_2)
        if num < 10 and num_2 < 10:
            print(f'"0{num} руб 0{num_2} коп"', end=" ")
        elif num > 10 and num_2 < 10:
            print(f'"{num} руб 0{num_2} коп"', end=" ")
        elif num < 10 and num_2 > 10:
            print(f'"0{num} руб {num_2} коп"', end=" ")
        else:
            print(f'"{num} руб {num_2} коп"', end=" ")
output()
lst.reverse()
output()