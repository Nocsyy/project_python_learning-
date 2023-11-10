class Entreprise:
    def __init__(self, name, adresse, siret):
        self.name = name
        self.adresse = adresse
        # Utilisation d'une méthode pour définir le SIRET
        self.set_siret(siret)

    def set_siret(self, siret):
        if not isinstance(siret, str) or not siret.isdigit() or len(siret) != 14:
            raise ValueError(
                "Le numéro SIRET doit être une chaîne de caractères composée de 14 chiffres.")
        self.siret = siret

    def __str__(self):
        return f"Entreprise: {self.name}, Adresse: {self.adresse}, SIRET: {self.siret}"


# Création de l'instance
try:
    entreprise = Entreprise(
        "Ma Société", "123 rue de la République", "01234567890123")
except ValueError as e:
    print(e)
print(entreprise)


# Crétion de la boucle while pour gérer l'ajout du nouveau siret
while True:
    new_siret = input(
        "Veuillez entrer le nouveau numéro SIRET à 14 chiffres : ")
# Changement du numéro SIRET
    if len(new_siret) == 14 and new_siret.isdigit():
        try:
            entreprise.set_siret(new_siret)
            print("Mise à jour du SIRET effectuée.")
            print(entreprise)
            break
        except ValueError as e:
            print(e)
    else:
        print("Le SIRET doit être composé de 14 chiffres.")
