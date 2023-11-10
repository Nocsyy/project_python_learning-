from model.compte import CompteBancaire
from model.client import Client

compte1 = CompteBancaire('2023-11-06', Client('Doe', 'John',
                         '123 rue de la Paix', '123456789012345'), 1000.0)
compte2 = CompteBancaire('2023-11-06', Client('Smith', 'Jane',
                         '456 avenue de la Liberté', '987654321098765'), 1000.0)

# Print leur identifiant interne respectif
print(f"L'identifiant du compte 1 est: {compte1.identifiant}")
print(f"L'identifiant du compte 2 est: {compte2.identifiant}")

# Print leur égalité l'un avec l'autre
print(
    f"Les deux comptes sont-ils égaux? {'Oui' if compte1 == compte2 else 'Non'}")

# Print le solde total de tous les comptes bancaires créés
print(
    f"Le solde total de la banque est: {CompteBancaire.get_total_soldes()} euros")
