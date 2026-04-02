# Nom : Angel
# Ce programme trouve combien de jours il y a en moyenne dans un mois,
# pour une annee normale et une annee bissextile.
 
# Une annee normale a 365 jours. Je divise par 12 mois pour avoir la moyenne.
moyenne_normale = 365 / 12
 
# Une annee bissextile a 366 jours (fevrier a 29 jours au lieu de 28).
moyenne_bissextile = 366 / 12
 
# print() ca affiche un message a l'ecran pour que l'utilisateur voit le resultat.
# Le f"..." permet de mettre une variable dans le texte avec {}.
# Le :.2f dit a Python d'afficher seulement 2 chiffres apres la virgule (ex: 30.42).
print(f"Annee normale    : {moyenne_normale:.2f} jours par mois en moyenne")
print(f"Annee bissextile : {moyenne_bissextile:.2f} jours par mois en moyenne")