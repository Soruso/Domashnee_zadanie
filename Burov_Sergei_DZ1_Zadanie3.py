def get_declension(i):
    result = ""
    if i >= 11 and i <= 14:
        result = "процентов"
    elif i % 10 == 1:
        result = "процент"
    elif i % 10 >= 5 and i % 10 <= 9 or i % 10 ==0:
        result = "процентов"
    elif i % 10 >= 2 and i % 10 <= 4:
        result = "процента"
    return result

for i in range(1,101):
    s = get_declension(i)
    print(i, s)