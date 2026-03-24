def peut_entrer(age):
    return age >= 18

age_utilisateur = int(input("Quel est votre âge ? "))

if peut_entrer(age_utilisateur):
    print("Bienvenue au club !")
else:
    print("Désolé, vous êtes trop jeune.")