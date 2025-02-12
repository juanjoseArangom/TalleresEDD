felipe = set()
vanesa = set()
 
while True:
    entrada = input().strip()
    if entrada == '#':
        break
    quien, pokemon = entrada.split()
    if quien == 'F':
        felipe.add(pokemon)
    else:
        vanesa.add(pokemon)
 
total_felipe = len(felipe)
total_vanesa = len(vanesa)
total_conjunto = len(felipe.union(vanesa))
 
print(total_felipe, total_vanesa, total_conjunto)