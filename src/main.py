from code import *
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
#f1 = uma.code()
#f2 = duas.code()
#f3 = tres.code()
#f1_f2 = compare(f1,f2)
#print "f1 - f2: %s" % f1_f2
#f1_f3 = compare(f1,f3)
#print "f1 - f3: %s" % f1_f3
#f2_f3 = compare(f2,f3)
#print "f2 - f3: %s" % f2_f3
#f1_f1 = compare(f1,f1)
#print "f1 - f1: %s" % f1_f1
#f1_f1 = compare(f1,f1)
#print "f1 - f1: %s" % f1_f1
#f3_f3 = compare(f3,f3)
#print "f3 - f3: %s" % f3_f3
#f2_f2 = compare(f2,f2)
#print "f2 - f2: %s" % f2_f2
#a = f1
#print "A"
#print a

print
print "G A U S S I A N"
print
uma = Gaussian("mirror.jpg", 0.9)
duas = Gaussian("mirror.jpg", 0.9)
tres = Gaussian("people.jpg", 0.9)
#f1 = uma.code()
#f2 = duas.code()
#b = f1
#c = f2
#f2 = duas.code()
#f3 = tres.code()
#f1_f2 = compare(f1,f2)
#print "f1 - f2: %s" % f1_f2
#f1_f3 = compare(f1,f3)
#print "f1 - f3: %s" % f1_f3
#f2_f3 = compare(f2,f3)
#print "f2 - f3: %s" % f2_f3
#f1_f1 = compare(f1,f1)
#print "f1 - f1: %s" % f1_f1
#f1_f1 = compare(f1,f1)
#print "f1 - f1: %s" % f1_f1
#f3_f3 = compare(f3,f3)
#print "f3 - f3: %s" % f3_f3
#f2_f2 = compare(f2,f2)
#print "f2 - f2: %s" % f2_f2


print "B"
print b
print "C"
print c
#f1 = uma.LDNgCode()
#f2 = duas.LDNgCode()
#f3 = tres.LDNgCode()
#f1__f2 = compare(f1,f2)
#f1__f3 = compare(f1,f3)

