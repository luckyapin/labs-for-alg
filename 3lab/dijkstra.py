def newd(streets,i):
    newmin = float('inf')
    
    for j in range(len(d)):
        if not d[j][1]: #Если вершина ней пройдена

            tekmin = min(d[j][0], round(d[i][0] + streets[i][j],1)) 
            if  (d[i][0] + streets[i][j]) < d[j][0]: 
                d[j][2] = i #Для сохранения откуда мы пришли в эту точку
            d[j][0] = tekmin

            #Запоминаем индекс минимального расстояния
            if newmin > tekmin:
                newmin = tekmin
                newindex = j
            
    return newindex
#Главная функция для импорта
def result(streets,start):
    n = float('inf')
    #Делаем d глобальной, её можно было использовать в другой функции   
    global d
    #d массив, хранящий кратчайшие пути, пройдена ли она и откуда эта вершина взята 
    d = [] 
    
    newmin = start
    #Заполняем начальными значениями массив d
    for _ in range(len(streets)):
        d.append([n, False, False])
    #значения начальной точки
    d[newmin]=[0, True, 0]
    #Функция выдает индекс минимальной непройденной вершины, для последующей её проверки 
    for _ in range(len(d) - 1):
        newmin = newd(streets, newmin)
        d[newmin][1] = True

    res_d=[]
    res_graph=[]
    #Заполняеем вывод
    res_d=[[x[0]] for x in d]
    res_graph=[(d[x][2], x) for x in range(len(d))]

    return [res_d, res_graph]

