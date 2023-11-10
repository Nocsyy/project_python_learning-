from datetime import datetime


def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%d/%m/%Y')
        return True
    except ValueError:
        print("La date de sortie n'est pas valide. Veuillez utiliser le format DD/MM/YYYY.")
        return False
