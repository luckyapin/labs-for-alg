
message='10010000011000101000011101010101001001011'

#исключающее ИЛИ (работает только для данной задачи - одна длина)
def XOR(c1,c2):
    return ''.join(map(str,[abs(int(c1[i]==c2[i])-1) for i in range(len(c1))]))

#метод побитового сдвига
P=bin(int('814141ab',16))[2:]
#CRC-32

def csc_1(message):
    i=0
    k=32
    delim=message[i:k]
    ost = XOR(delim, P)
    sdvig = ost.find('1')
    i = k
    k += sdvig

    while k<=len(message)-1:
        delim=ost[sdvig:]+message[i:k]
        ost=XOR(delim,P)
        sdvig = ost.find('1')
        i = k
        if k+sdvig>len(message)-1:
            delim = ost[ost.find('1'):] + message[i:]
            ost=delim
            break
        else:
            k += sdvig
            
    print(f"Контрольная сумма: {ost[ost.find('1'):]}")

csc_1(message)




