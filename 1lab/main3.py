import random
from shapely.geometry import LineString



#создание четырехугольников (координаты)
N = int(input("Введите количество четырехугольников: "))
ch = [[] for _ in range(N)]
i = 0
while i<N:
    tochka = set()
    while len(ch[i])!=4:
        x,y = random.randint(1,100), random.randint(1,100)
        if (x,y) not in tochka:
            ch[i].append((x,y))
        tochka.add((x, y))
    A = LineString([ch[i][0], ch[i][1]])
    B = LineString([ch[i][1], ch[i][2]])
    C = LineString([ch[i][2], ch[i][3]])
    D = LineString([ch[i][3], ch[i][0]])
    if not ((A.intersects(C) == False) and (B.intersects(D) == False)):
        ch[i]=[]
    else:
        ch[i] = [A, B, C, D]
        i+=1

stroka = ""
sl={0: 'A', 1: 'B', 2: 'C', 3: 'D'}
for i in range(N):
    for j in range(i+1,N):
        l=""
        for storona1 in range(4):
            for storona2 in range(4):
                if ch[i][storona1].intersects(ch[j][storona2]):
                    l+=(sl[storona1]+sl[storona2])
        stroka += l
        print(f"Пересечения {i+1} и {j+1} четырехугольника: {l}")


print("Строка пересечений: ", stroka)



def knyt(line, template):
    pref_for_template=pref(template) #поиск префикс-функции для шаблона
    cnt=0
    pos=0
    while True:
        
        tline=line[pos:pos+len(template)]
        
        if len(template)>len(tline): #если pos будет правее, чем нужно, значит мы прошли через всю строку
            return None,None
        shift=comp(tline,template) #номер в массиве префикс-функции шаблона, а так же номер несовпавшего элемента в шаблоне
        
        if shift is not None: #если функция comp что-то вывела
            pos+=pref_for_template[shift]+1 #сдвиг 
        else:
            return template,pos
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

def RabinKarp(string, pattern):
    n, m = len(string), len(pattern)    
    count=0
    hpattern = hash(pattern)    
    for i in range(n-m+1):
            hs = hash(string[i:i+m])        
            if hs == hpattern:
                if string[i:i+m] == pattern:                
                    return i
    return None
    
a=stroka
maxl=0
maxPlace=0
mtemp=''
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        
        temp,place1=knyt(a,a[i:j]+a[i:j][::-1])
        temp,place2= knyt(a,a[i:j]+a[i:j-1][::-1])
        
        if place1 is not None:
            if j-i>maxl:
                maxl=j-i
                maxPlace=place1
                mtemp=temp
        if place2 is not None:
            if j-i>maxl:
                maxl=j-i
                maxPlace=place2
                mtemp=temp
                

print("Кнут-Моррис-Пратт: ",mtemp,maxPlace)

mas=['A','B','C','D']
maxst=''

for i in range(len(a)-1):
    
    for j in range(i+1,len(a)):
        c=2
        
        st=a[i:j]
        for k in a:
            if st.count(k) %2!=0:
                c-=1
        if c>0:
            
            if len(st)>len(maxst):
                maxst=st

print("Рабин-Карп: ", maxst, RabinKarp(a,maxst))
