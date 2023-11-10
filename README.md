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
  
## Exercice 2
## Exercice 3
## Exercice 4
