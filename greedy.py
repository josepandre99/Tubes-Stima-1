def cek( val , n ) :
    c = []
    c.append(abs(24-(int(val)+int(n))))
    c.append(abs(24-(int(val)-int(n))))
    c.append(abs(24-(int(val)*int(n))))
    c.append(abs(24-(int(val)/int(n))))
    if (min(c) == c[0]) :
        return '+'
    elif (min(c) == c[1]) :
        return '-'
    elif (min(c) == c[2]) :
        return '*'
    else :
        return '/'


def hasil(l) :  
    ltemp = [int(i) for i in l]
    ltemp.sort(reverse = True)
    l = [str(i) for i in ltemp]

    value = 0
    s = []
    
    s = l[0]
    value = l[0]
    s = s + cek(value,l[1])
    s = s + (l[1])
    oprb = cek(value,l[1])
    value =  eval(s)
    s = s + cek(value,l[2])
    s = s + (l[2])
    if ((oprb == '+' or oprb == '-') and (cek(value,l[2]) == '*' or cek(value,l[2]) == '/')) :
        index = s.find(l[0])
        x = s[:index] + '(' + s[index:]
        s = x 
        index = s.find(cek(value,l[2]))
        x = s[:index] + ')' + s[index:]
        s = x
    oprbb = oprb
    oprb = cek(value,l[2])
    value = eval(s)
    s = s + cek(value,l[3])
    s = s + l[3]
    if (((oprbb == '+' or oprbb == '-') and (oprb == '+' or oprb == '-')) and (cek(value,l[3]) == '*' or cek(value,l[3]) == '/')) :
        index = s.find(l[0])
        x = s[:index] + '(' + s[index:]
        s = x
        index = s.find(cek(value,l[3]))
        x = s[:index] + ')' + s[index:]
        s = x
    elif ((oprb == '+' or oprb == '-') and (cek(value,l[3]) == '*' or cek(value,l[3]) == '/')) :
        index = s.find(l[1])
        x = s[:index] + '(' + s[index:]
        s = x
        index = s.find(cek(value,l[3]))
        x = s[:index] + ')' + s[index:]
        s = x
    return s
