conj1 = {1, 2, 3, 4, 5}
conj2 = {5, 6, 7, 8, 9, 10}

conj_new = conj1.union(conj2) # Unindo os conjuntos
print(conj_new)

conj_new.discard(7) # Retirando um elemento
print(conj_new)

conj_intersecc = conj1.intersection(conj2) # Elemento duplicado
print(conj_intersecc)
conjunto = {1, 2, 2, 1, 4, 5}
