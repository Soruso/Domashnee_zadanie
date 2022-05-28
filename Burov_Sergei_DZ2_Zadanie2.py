lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
lst.insert(1,'"')
lst.insert(3,'"')
lst.insert(5,'"')
lst.insert(7,'"')
lst.insert(12,'"')
lst.insert(14,'"')
lst[2] = '05'
lst[13] = '+05'
print(f'{lst[0]} {lst[1]}{lst[2]}{lst[3]} {lst[4]} {lst[5]}{lst[6]}{lst[7]} {lst[8]} {lst[9]} {lst[10]} {lst[11]} {lst[12]}{lst[13]}{lst[14]} {lst[15]}')