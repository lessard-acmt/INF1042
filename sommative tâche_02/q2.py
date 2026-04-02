# Nom : Angel
# Ce programme demande une temperature en Celsius et la convertit
# en Fahrenheit et en Kelvin.
 
# input() pose une question a l'utilisateur et attend sa reponse.
# float() convertit la reponse en nombre avec decimales (ex: 36.6).
# On garde le resultat dans une variable appelee celsius.
celsius = float(input("Entrez une temperature en Celsius : "))
 
# Formule pour Fahrenheit : multiplier par 9, diviser par 5, ajouter 32.
fahrenheit = (celsius * 9 / 5) + 32
 
# Formule pour Kelvin : juste ajouter 273.15 au Celsius.
kelvin = celsius + 273.15
 
# On affiche les deux resultats avec 2 decimales.
print(f"{celsius} degres Celsius = {fahrenheit:.2f} degres Fahrenheit")
print(f"{celsius} degres Celsius = {kelvin:.2f} Kelvin")