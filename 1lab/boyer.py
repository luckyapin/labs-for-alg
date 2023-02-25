def boyer(line, template):
    pos=0
    cnt=0
    length=len(template)
    while True:
        tline=line[pos:pos+length]

        if len(template)>len(tline): #если pos будет правее, чем нужно, значит мы прошли через всю строку
            return cnt
        pos_in_line, letter=comp(tline,template) #несходящаяся буква


        if letter: 
            searching_template=template[:pos_in_line-1]
            if letter in searching_template: #если буква есть в шаблоне, значит совмещаем одинаковые буквы

                pos_in_template=searching_template.rfind(letter)+1
                pos+=pos_in_line-pos_in_template
            else: #если буквы нет, то сдвигаемся на длину шаблона
                pos+=pos_in_line
        else: #если в letter False, значит строки одинаковые
            cnt+=1
            pos+=1
            

def comp(tline,template): #функция для проверки совпадений между текущей строкой и шаблоном
    if tline[-1]==template[-1]:
        if len(tline)==1:
            return (False,False) 
        return comp(tline[0:-1],template[0:-1]) #рекурсивная проверка слева направо теперь для строки с длиной на 1 меньше
    else:
        return (len(template),tline[-1]) #если найдено несовпадение букв, выдает несовпавшую букву








