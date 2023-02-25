from boyer import *
from knyt import *


f1,f2=0,1
s='01'
for i in range(2,500):
    f1,f2=f2,f1+f2
    s+=str(f2)
mas=[0]*100

for i in range(10,100):
    
    mas[i]=boyer(s,str(i))
print('По Бойеру: ')
print('Самое частое число: ',mas.index(max(mas)))
print('Встречается ',max(mas),' раз')
for i in range(10,100):
    mas[i]=knyt(s[:],str(i))

print('По Кнуту: ')
print('Самое частое число: ',mas.index(max(mas)))
print('Встречается ',max(mas),' раз')