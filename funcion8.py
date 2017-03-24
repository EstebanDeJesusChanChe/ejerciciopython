print "_______________________________________________"
print "Generar un intervalo de n numeros entre 20 y 60"
print "_______________________________________________"

n = 20
h = ''
while n <= 60:
    if n%2 == 0:
        h += ' %i' % n
    n += 1
print h