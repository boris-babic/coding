t1 = 5.33*10**-4
t2 = 5.25*10**-4
vl = 3 * 10**8 #rychlost tych vln
s1 = t1 * vl / 2 #vzdialenost od radaru pri 1. merani
s2 = t2 * vl / 2 #vzdialenost pri 2. merani
s = abs(s1 - s2) #prejdena vzdialenost
v = s / 5 * 3.6 #presiel to za 5 sekund
print(f"Rychlost, ktorou sa lietadlo priblizuje k radaru je {v}km/s.")