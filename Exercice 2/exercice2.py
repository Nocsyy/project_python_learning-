from dataclasses import dataclass


@dataclass
class DatabaseConnection:
    type_base: str
    user: str
    password: str
    hote: str = "localhost"

    nb_instances: int = 0

    def __post_init__(self):
        # Incrémente le nombre d'instance à chaque fois qu'une nouvelle instance est créée.
        DatabaseConnection.nb_instances += 1

    @staticmethod
    def get_nb_instance():

        return f"La classe DatabaseConnection possède actuellement {DatabaseConnection.nb_instances} instance(s)."

    @classmethod
    def create_mariadb_instance(cls):

        return cls(type_base="mariadb", user="root", password="1234", hote="76.287.872.12")


db_conn1 = DatabaseConnection(
    type_base="MySQL", user="admin", password="password")
print(db_conn1)


db_conn2 = DatabaseConnection.create_mariadb_instance()
print(db_conn2)


print(DatabaseConnection.get_nb_instance())
