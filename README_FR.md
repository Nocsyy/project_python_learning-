# project_python_learning-

# Exercice 1 - Classe Entreprise

## Description

Cet exercice a pour but de créer une classe `Entreprise` qui contiendra des informations de base telles que le nom de l'entreprise, son adresse et son numéro de SIRET. Le numéro de SIRET est un identifiant unique composé de 14 chiffres.

## Objectifs

1. **Création de la classe `Entreprise`**:
   - La classe doit avoir les attributs suivants :
     - `nom` : Le nom de l'entreprise.
     - `adresse` : L'adresse du siège social de l'entreprise.
     - `siret` : Le numéro de SIRET de l'entreprise.

2. **Affichage personnalisé**:
   - L'affichage d'un objet de la classe `Entreprise` doit suivre ce format : "L'entreprise {nom}, ayant son siège social au {adresse}, possède le numéro de SIRET {siret}".

3. **Tests de la classe**:
   - Création d'une instance de la classe `Entreprise`.
   - Affichage de l'instance pour vérifier le format de sortie.
   - Affichage du nom de l'entreprise.
   - Modification du numéro de SIRET de l'entreprise et affichage de l'objet pour observer le changement.

## Consignes

- Assurez-vous que le code est propre et clair.
- Vérifiez que le numéro de SIRET est toujours composé de 14 chiffres.
- Gérez correctement les erreurs et les entrées invalides.

## Exemple de sortie attendue

```python
  # Création de l'instance
  entreprise = Entreprise("TechCorp", "123 Avenue de l'Innovation, 75000 Paris", "12345678901234")
  
  # Affichage de l'entreprise
  print(entreprise) 
  # Sortie: "L'entreprise TechCorp, ayant son siège social au 123 Avenue de l'Innovation, 75000 Paris, possède le numéro de SIRET 12345678901234"
  
  # Affichage du nom
  print(entreprise.nom) 
  # Sortie: "TechCorp"
  
  # Modification du numéro de SIRET
  entreprise.siret = "43210987654321"
  print(entreprise) 
# Sortie: "L'entreprise TechCorp, ayant son siège social au 123 Avenue de l'Innovation, 75000 Paris, possède le numéro de SIRET 43210987654321"
```

# Exercice 2 - Classe DatabaseConnection avec Dataclass

## Description

Cet exercice consiste à utiliser une `dataclass` pour créer une classe `DatabaseConnection`. Cette classe représente une connexion à une base de données et contient les informations suivantes : type de base de données (MySQL, MariaDB, PostgreSQL, etc.), utilisateur, mot de passe, et hôte. Par défaut, l'hôte est défini sur "localhost".

## Objectifs

1. **Création de la classe `DatabaseConnection`**:
   - La classe doit être une `dataclass` contenant les attributs suivants :
     - `type_base` : Type de la base de données (string).
     - `user` : Nom de l'utilisateur (string).
     - `password` : Mot de passe (string).
     - `hote` : Hôte de la base de données (string) avec une valeur par défaut "localhost".

2. **Propriété statique `nb_instances`**:
   - La classe doit avoir une propriété statique `nb_instances` qui s'incrémente automatiquement à chaque création d'une nouvelle instance.

3. **Méthodes de la classe**:
   - Une méthode statique pour retourner le nombre total d'instances sous la forme : "La classe DatabaseConnection possède actuellement {x} instance(s)."
   - Une méthode de classe `create_mariadb_instance` pour créer une instance avec des valeurs prédéfinies.

4. **Tests de la classe**:
   - Initialiser un objet de cette classe sans spécifier l'hôte et afficher le résultat.
   - Initialiser un objet en utilisant la méthode `create_mariadb_instance` et afficher le résultat.
   - Afficher le nombre total d'instances créées.

## Exemple de Code

```python
from dataclasses import dataclass

@dataclass
class DatabaseConnection:
    # Définition de la classe avec les attributs nécessaires
    ...

# Initialisation et affichage de la première instance
db_conn1 = DatabaseConnection(type_base="MySQL", user="admin", password="password")
print(db_conn1)

# Initialisation et affichage de la deuxième instance via la factory
db_conn2 = DatabaseConnection.create_mariadb_instance()
print(db_conn2)

# Affichage du nombre total d'instances
print(DatabaseConnection.get_nb_instance())
```

## Exemple de sortie attendue
   ```python
DatabaseConnection(type_base='MySQL', user='admin', password='password', hote='localhost')
DatabaseConnection(type_base='mariadb', user='root', password='1234', hote='76.287.872.12')
La classe DatabaseConnection possède actuellement 2 instance(s).
   ````
# Exercice 3 - Classes Client et CompteBancaire

## Description

L'objectif de cet exercice est de créer deux classes : `Client` et `CompteBancaire`. La classe `Client` doit contenir des informations personnelles, tandis que `CompteBancaire` doit gérer des informations liées aux comptes bancaires des clients.

## Objectifs

1. **Classe `Client`**:
   - Attributs : nom, prénom, adresse, numéro de sécurité sociale (NIR) composé de 15 chiffres.
   - Contrôle du NIR lors de la création de l'objet.

2. **Classe `CompteBancaire`**:
   - Constructeur acceptant trois paramètres : date de création (string au format "YYYY-MM-DD"), client (de type `Client`), et solde (float).
   - Quatre propriétés :
     - Date de création (convertie en format date).
     - Client (de type `Client`).
     - Identifiant interne (4 lettres majuscules aléatoires suivies de la date de création au format DDMMYYYY).
     - Solde (float).
   - Propriété statique pour la somme des soldes de tous les comptes.
   - Égalité de deux comptes basée sur l'égalité de leurs soldes.

3. **Tests de la classe `CompteBancaire`**:
   - Créer deux comptes bancaires.
   - Afficher leurs identifiants internes.
   - Vérifier et afficher s'ils sont égaux.
   - Afficher le solde total de tous les comptes bancaires.

## Exemple de Code

```python
# Définition des classes Client et CompteBancaire
...

# Création et affichage des comptes bancaires
compte1 = CompteBancaire("2023-01-01", client1, 1000.0)
compte2 = CompteBancaire("2023-01-02", client2, 2000.0)

print(compte1.identifiant)
print(compte2.identifiant)
print(compte1 == compte2)

# Affichage du solde total
print(CompteBancaire.solde_total())
```
## Exemple de sortie attendue
```python
Identifiant du compte1 : Exemple XYZ12301012023
Identifiant du compte2 : Exemple ABC12302012023
Les deux comptes sont-ils égaux ? False
Solde total des comptes : 3000.0
```
# Exercice 4 - Classe Movie et Gestion de Films

## Description

Cet exercice implique la création d'une classe `Movie` pour gérer une collection de films. Cette classe gérera les informations des films et interagira avec un fichier JSON pour stocker ces données.

## Objectifs

1. **Classe `Movie`**:
   - Attributs : titre (string), date de sortie (string au format DD/MM/YYYY), et résumé (string).
   - Création d'un fichier JSON dans un dossier `data` lors de la première instance de `Movie`, si ce fichier n'existe pas.
   - Ajout de nouvelles instances de `Movie` dans le fichier JSON.
   - Méthode pour supprimer un film de la liste dans le fichier JSON.
   - Méthodes pour modifier le titre, la date de sortie ou le résumé d'un film.
   - Méthode pour afficher les informations d'un film à partir de son titre.

2. **Application de Terminal**:
   - Fonctionnalité `create` pour ajouter un nouveau film.
   - Fonctionnalité `read` pour lire les informations d'un film spécifique ou afficher tous les films par ordre croissant de date de sortie.
   - Fonctionnalité `update` pour modifier les informations d'un film.
   - Fonctionnalité `delete` pour supprimer un film.
   - Les recherches par titre de film fonctionnent indépendamment de la casse.
   - Les titres de films sont stockés avec une majuscule à chaque mot.

## Exemple de Code

```python
# Définition de la classe Movie et des méthodes pour gérer le fichier JSON
...

# Exemples d'utilisation des commandes dans l'application de terminal
# create, read, update, delete
...
```
##Exemple de sortie attendue
```python 
# Après avoir exécuté une commande 'create'
Liste complète des films après ajout: [...]

# Après avoir exécuté une commande 'read'
Informations du film recherché: [...]

# Après avoir exécuté une commande 'update'
Film après modification: [...]

# Après avoir exécuté une commande 'delete'
Liste complète des films après suppression: [...]

{
    "movies": [
        {
            "titre": "The Dark Knight, Le Chevalier Noir",
            "date_de_sortie": "13/08/2008",
            "description": "Dans ce nouveau volet, Batman augmente les mises dans sa guerre contre le crime. Avec l'appui du lieutenant de police Jim Gordon et du procureur de Gotham, Harvey Dent, Batman vise à éradiquer le crime organisé qui pullule dans la ville. Leur association est très efficace mais elle sera bientôt bouleversée par le chaos d'éclenché par un criminel extraordinaire que les citoyens de Gotham connaissent sous le nom de Joker."
        }
    ]
}
```
