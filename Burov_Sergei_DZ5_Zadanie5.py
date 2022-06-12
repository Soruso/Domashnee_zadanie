src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def f1(ls):
    result = []
    for i in range(len(ls)):
        dublicates_found = False
        for x in range(len(ls)):
            if i != x and ls[i] == ls[x]:
                dublicates_found = True
                break
        if not dublicates_found:
            result.append(ls[i])

    return result


res = f1(src)
print(res)
