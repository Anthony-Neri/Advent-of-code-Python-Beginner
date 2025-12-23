import time

# Récupération des données

start = time.perf_counter()
total_token = 0

for block in data:
    button_a = block[0]
    button_b = block[1]
    prize = block[2]


    a = button_a[0]
    b = button_b[0]
    c = button_a[1]
    d = button_b[1]
    e = prize[0] + 10000000000000
    f = prize[1] + 10000000000000
 
    # a * x + b * y = e
    # c * x + d * y = f
    # x = pression bouton A. a pour la valeur X et c pour la valeur Y.
    # y = pression bouton B. b pour la valeur X et d pout la valeur Y.
    # Pour le premier exemple :  *
    # 94x + 22y = 8400
    # 34x + 67y = 5400
    # => Resolution système à deux inconnues

    y = ((e*c)-(a*f)) / ((-d*a) + (b*c))

    x = (f-(d*y))/c

    if y.is_integer() and x.is_integer():
        total_token+=y+x*3

print(total_token)

end = time.perf_counter()
print(f"Temps d'exécution : {(end - start)*1000:.3f} ms")
