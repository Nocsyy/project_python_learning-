class Client:
    def __init__(self, name, first_name, adresse, nir):
        self.name = name
        self.first_name = first_name
        self.adresse = adresse
        self.set_nir(nir)

    def set_nir(self, nir):
        if not isinstance(nir, str) or not nir.isdigit() or len(nir) != 15:
            raise ValueError(
                "Le numéro NIR doit être une chaîne de caractères composée de 15 chiffres.")
        self.nir = nir
