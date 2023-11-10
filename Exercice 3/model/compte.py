from .client import Client
from datetime import datetime
import random
import string


total_bank_balance = 0


class CompteBancaire:
    total_soldes = 0

    def __init__(self, date_creation: str, client: Client, solde: float):
        self.date_creation = datetime.strptime(date_creation, "%Y-%m-%d")
        self.client = client
        self.identifiant = self.generate_identifiant()
        self.solde = solde
        CompteBancaire.total_soldes += solde

    def generate_identifiant(self):
        lettres = ''.join(random.choices(string.ascii_uppercase, k=4))
        date_formattee = self.date_creation.strftime("%d%m%Y")
        return f"{lettres}{date_formattee}"

    @staticmethod
    def get_total_soldes():
        return CompteBancaire.total_soldes

    def __eq__(self, other):
        if isinstance(other, CompteBancaire):
            return self.solde == other.solde
        return False
