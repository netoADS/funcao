def ano_bi(ano):
    if ano % 4 != 0:
        return False
    elif ano % 100 != 0:
        return True
    elif ano % 400 != 0:
        return False
    else:
        return True
        
#anos para comparar
dt = [1900,2000,2016,1987,2020]
#resultado real
rr = [False,True,True,False,True]
#checar função
for i in range(len(dt)):
    yr = dt[i]
    print(yr, '-> ', end='')
    result = ano_bi(yr)
    if result == rr[i]:
        print('ok')
    else:
        print('Falha')