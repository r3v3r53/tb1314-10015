from LH import LH

def compare(f1, f2, i = None, val = 0):
    if i == None: i = len(f1)
    if i == 0: return val
    i -= 1
    if f1[i] + f2[i] != 0:
        val += ((f1[i] - f2[i])**2 / (f1[i] + f2[i]))
    return compare(f1, f2, i, val)


uma = LH("mirror.jpg")
duas = LH("mirror2.jpg")
tres = LH("people.jpg")
f1 = uma.code()
f2 = duas.code()
f3 = tres.code()
f1_f2 = compare(f1,f2)
f1_f3 = compare(f1,f3)

print f1_f2, f1_f3

