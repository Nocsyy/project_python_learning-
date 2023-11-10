from model.movie import Movie
from model.date import validate_date


def main():
    print("Bienvenue")
    while True:
        command = input(
            "Choisissez une commande (créer, lire, modifier, supprimer, annuler) : ").lower()

# commande de création

        if command == 'créer':
            title = input("Entrez le titre du film : ")
            release_date = input("Entrez la date de sortie (DD/MM/YYYY) : ")
            if not validate_date(release_date):
                continue
            description = input("Entrez la description du film : ")
            Movie(title, release_date, description)
            Movie.print_all_movies()

# commande de lecture

        elif command == 'lire':
            read_choice = input(
                "Vous souhaitez lire un seul film ou tous les films (un/tout) : ").lower()
            if read_choice == 'un':
                title = input("Entrez le titre du film : ")
                Movie.print_movie(title)
            elif read_choice == 'tout':
                Movie.print_all_movies()
            else:
                print("Choix invalide, choisissez un ou tout")

# commande de modification

        elif command == 'modifier':
            title = input("Entrez le titre du film à modifier : ").strip()
            if Movie.movie_exists(title):
                property_to_update = input(
                    "Que voulez-vous modifier ? (titre/date_de_sortie/description) : ").lower().strip()

                valid_properties = ['titre', 'date_de_sortie', 'description']
                if property_to_update in valid_properties:
                    new_value = input(
                        f"Entrez la nouvelle valeur pour {property_to_update}: ").strip()

                    if property_to_update == 'date_de_sortie':

                        if not validate_date(new_value):
                            print("Veuillez entrer une date au format DD/MM/YYYY.")
                            continue

                    if Movie.update_movie(title, property_to_update, new_value):
                        print("Le film a été mis à jour avec succès.")
                    else:
                        print(
                            "Une erreur s'est produite lors de la mise à jour du film.")
                else:
                    print(
                        "Propriété non valide. Entrez 'titre', 'date_de_sortie' ou 'description'.")
            else:
                print("Le film n'existe pas. Veuillez essayer un autre titre.")

# commande de suppression
        elif command == 'supprimer':
            title = input("Entrer le titre du film a supprimer : ")
            if Movie.movie_exists(title):
                Movie.delete_movie(title)
                Movie.print_all_movies()

            else:
                print("Entrez un film qui existe ")
 # commande d'annulation

        elif command == 'annuler':
            print("Annulation, fermeture du programme")
            break
        else:
            print(
                "Commande invalide, entrez une cimmande valide : créer, lire, modifier, supprimer, annuler ")


if __name__ == '__main__':
    main()
