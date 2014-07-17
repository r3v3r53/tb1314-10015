from code import *
def compare(f1, f2, i = None, val = 0):
    if i == None: i = len(f1)
    if i == 0: return val
    i -= 1
    if f1[i] + f2[i] != 0:
        val += ((f1[i] - f2[i])**2 / (f1[i] + f2[i]))
    return compare(f1, f2, i, val)


uma = Kirsh("mirror.jpg")
duas = Kirsh("mirror2.jpg")
#tres = LH("people.jpg", 0.3)
f1 = uma.code()
f2 = duas.code()
#f3 = tres.LDNkCode()
f1_f2 = compare(f1,f2)
f1_f3 = compare(f1,f3)

#f1 = uma.LDNgCode()
#f2 = duas.LDNgCode()
#f3 = tres.LDNgCode()
#f1__f2 = compare(f1,f2)
#f1__f3 = compare(f1,f3)


print f1_f2, f1_f3
#print f1__f2, f1__f3
