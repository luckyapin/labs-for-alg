from boyer import *
from knyt import *
from naive import *
from rabinkarp import *

f1,f2=0,1
s='01'
for i in range(2,500):
    f1,f2=f2,f1+f2
    s+=str(f2)
mas=[0]*100
sl={}
#1 - наивный
sl=naive(s)


print('Наивный:')

print('Самое частое число встречается',max(sl.values()),'раз')
#2 - Рубина-Карпа
ch=sl.keys()
for x in ch:    
     sl[x]=RabinKarp(s,x)

print('По Рабину-Карпу:')
print('Самое частое число встречается',max(sl.values()),'раз')
for i in range(10,100):
    
    mas[i]=boyer(s,str(i))
print('По Бойеру:')
print('Самое частое число встречается',max(mas),'раз')
for i in range(10,100):
    mas[i]=knyt(s,str(i))

print('По Кнуту:')
print('Самое частое число встречается',max(mas),'раз')


