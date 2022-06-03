def thesaurus(*names):
    list = {}
    for name in names:
        key = name[0].capitalize()
        if key not in list:
            list[key] = []
        list[key].append(name)
    return list
print(thesaurus("Иван", "Мария", "Петр", "Илья"))