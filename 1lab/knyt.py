def knyt(line, template):
    pref_for_template=pref(template) #поиск префикс-функции для шаблона
    cnt=0
    pos=0
    while True:
        
        tline=line[pos:pos+len(template)]
        
        if len(template)>len(tline): #если pos будет правее, чем нужно, значит мы прошли через всю строку
            return cnt
        shift=comp(tline,template) #номер в массиве префикс-функции шаблона, а так же номер несовпавшего элемента в шаблоне
        
        if shift is not None: #если функция comp что-то вывела
            pos+=pref_for_template[shift]+1 #сдвиг 
        else:
            
            pos+=1
            cnt+=1
    
def comp(tline,template): #функция для сравнения элеметов строки и шаблона
    for i in range(len(template)):
        if tline[i]!=template[i]:
            return i #если не равны выводит номер несовпавшего элемента
    #если нет несовпавших элеметов, значит функция выводит None
def pref(line):
    rez=[] 
    tline=''
    for j in line:
        tline+=j #формируем проверяемую строку
        c=0
       
        for i in range(len(tline)-1): #-1 т.к. не должно быть равно самой строке
            if tline[:i+1]== tline[-i-1:]: #до i-го элемента включительно и i+1 крайних элементов
                c=i+1
            
            
        rez.append(c)
    return rez




