temp = float(input("Température actuelle : "))
pluie = input("Est-ce qu'il pleut ? (oui/non) : ").lower()

# On vérifie les deux conditions avec 'and' et 'not'
if temp >= 15 and pluie == "non":
    print("Sortie permise")
else:
    print("On reste dedans")