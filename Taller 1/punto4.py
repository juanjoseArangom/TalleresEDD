n = int(input())
multiplos = []
if n % 2 == 0:
    multiplos.append("2")
if n % 3 == 0:
    multiplos.append("3")
if n % 5 == 0:
    multiplos.append("5")
if n % 7 == 0:
    multiplos.append("7")
if len(multiplos) == 0:
    print("no es multiplo de ninguno de los primeros cuatro primos")
else:
    print("es multiplo de " + multiplos[0])
    
