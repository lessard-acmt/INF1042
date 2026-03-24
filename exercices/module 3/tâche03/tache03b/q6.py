def est_pair(n):
    # L'opérateur % (modulo) donne le reste de la division par 2
    return n % 2 == 0

print(f"Est-ce que 10 est pair ? {est_pair(10)}")
print(f"Est-ce que 7 est pair ? {est_pair(7)}")