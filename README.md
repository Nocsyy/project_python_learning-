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
## Exercice 3
## Exercice 4
