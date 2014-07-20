from Kirsh import *

def compare(f1, f2, i = None, val = 0):
    if i == None: i = len(f1)
    if i == 0: return val
    i -= 1
    if f1[i] + f2[i] != 0:
        val += ((f1[i] - f2[i])**2 / (f1[i] + f2[i]))
    return compare(f1, f2, i, val)


print
print "K I R S H"
print
uma = Kirsh("mirror.jpg")
duas = Kirsh("mirror2.jpg")
tres = Kirsh("people.jpg")
f1 = uma.code()
f2 = duas.code()
f3 = tres.code()
f1_f2 = compare(f1,f2)
print "f1 - f2: %s" % f1_f2
f1_f3 = compare(f1,f3)
print "f1 - f3: %s" % f1_f3
f2_f3 = compare(f2,f3)
print "f2 - f3: %s" % f2_f3
