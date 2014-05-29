from LH import LH

def compare(f1, f2):
    result = 0.0
    temp = None
    for i in range(len(f1)):
        if f1[i] + f2[i] != 0:
            if temp == None:
                temp = ((f1[i] - f2[i])**2 / (f1[i] + f2[i]))
            else:
                temp = temp + ((f1[i] - f2[i])**2 / (f1[i] + f2[i]))
       
#        result += ((f1[i] - f2[i])**2)/(f1[i] + f2[i])
    return temp


uma = LH("mirror.jpg")
duas = LH("mirror2.jpg")
tres = LH("people.jpg")
f1 = uma.code()
f2 = duas.code()
f3 = tres.code()
f1_f2 = compare(f1,f2)
f1_f3 = compare(f1,f3)

print f1_f2, f1_f3
#(f1 -f2)^2 / f1+f2

#print a
