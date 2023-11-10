# Exercise 1 – Business Class

## Description

This exercise aims to create a `Company` class which will contain basic information such as the name of the company, its address and its SIRET number. The SIRET number is a unique identifier made up of 14 digits.

## Goals

1. **Creation of the `Company` class**:
    - The class must have the following attributes:
      - `name`: The name of the company.
      - `address`: The address of the company's head office.
      - `siret`: The company’s SIRET number.

2. **Custom Display**:
    - The display of an object of the `Company` class must follow this format: "The company {name}, having its head office at {address}, has the SIRET number {siret}".

3. **Class tests**:
    - Creation of an instance of the `Enterprise` class.
    - Display instance to check output format.
    - Display of company name.
    - Modification of the company's SIRET number and display of the object to observe the change.

## Instructions

- Make sure the code is clean and clear.
- Check that the SIRET number is always made up of 14 digits.
- Properly handle errors and invalid entries.

## Example of expected output

```python
   # Creation of the instance
   company = Company("TechCorp", "123 Avenue de l'Innovation, 75000 Paris", "12345678901234")
  
   # Company display
   print(company)
   # Output: "The company TechCorp, having its head office at 123 Avenue de l'Innovation, 75000 Paris, has the SIRET number 12345678901234"
  
   # Name display
   print(company.name)
   # Release: "TechCorp"
  
   # Modification of the SIRET number
   company.siret = "43210987654321"
   print(company)
# Output: "The company TechCorp, having its head office at 123 Avenue de l'Innovation, 75000 Paris, has the SIRET number 43210987654321"
```

# Exercise 2 – DatabaseConnection class with Dataclass

## Description

This exercise involves using a `dataclass` to create a `DatabaseConnection` class. This class represents a database connection and contains the following information: database type (MySQL, MariaDB, PostgreSQL, etc.), user, password, and host. By default, the host is set to "localhost".

## Goals

1. **Creation of the `DatabaseConnection`** class:
    - The class must be a `dataclass` containing the following attributes:
      - `base_type`: Database type (string).
      - `user`: User name (string).
      - `password`: Password (string).
      - `host`: Database host (string) with a default value of “localhost”.

2. **Static property `nb_instances`**:
    - The class must have a static property `nb_instances` which is automatically incremented each time a new instance is created.

3. **Class Methods**:
    - A static method to return the total number of instances in the form: "Class DatabaseConnection currently has {x} instance(s)."
    - A `create_mariadb_instance` class method to create an instance with predefined values.

4. **Class tests**:
    - Initialize an object of this class without specifying the host and display the result.
    - Initialize an object using the `create_mariadb_instance` method and display the result.
    - Show the total number of instances created.

## Code Example

```python
from dataclasses import dataclass

@dataclass
class DatabaseConnection:
     # Definition of class with necessary attributes
     ...

# Initialization and display of the first instance
db_conn1 = DatabaseConnection(type_base="MySQL", user="admin", password="password")
print(db_conn1)

# Initialization and display of the second instance via the factory
db_conn2 = DatabaseConnection.create_mariadb_instance()
print(db_conn2)

# Displaying the total number of instances
print(DatabaseConnection.get_nb_instance())
```

## Example of expected output
```python
DatabaseConnection(base_type='MySQL', user='admin', password='password', host='localhost')
DatabaseConnection(base_type='mariadb', user='root', password='1234', host='76.287.872.12')
The DatabaseConnection class currently has 2 instance(s).
````

# Exercise 3 - Customer and Bank Account Classes

## Description

The objective of this exercise is to create two classes: `Customer` and `Bank Account`. The `Customer` class must contain personal information, while `BankAccount` must manage information related to customers' bank accounts.

## Goals

1. **Class `Client`**:
    - Attributes: last name, first name, address, social security number (NIR) composed of 15 digits.
    - NIR control during object creation.

2. **Class `BankAccount`**:
    - Constructor accepting three parameters: creation date (string in "YYYY-MM-DD" format), customer (of type `Customer`), and balance (float).
    - Four properties:
      - Creation date (converted to date format).
      - Client (of type `Client`).
      - Internal identifier (4 random capital letters followed by the creation date in DDMMYYYY format).
      - Balance (float).
    - Static property for the sum of balances of all accounts.
    - Equality of two accounts based on the equality of their balances.

3. **Tests of the `BankAccount` class**:
    - Create two bank accounts.
    - View their internal identifiers.
    - Check and display if they are equal.
    - View the total balance of all bank accounts.

## Code Example

```python
# Definition of the Customer and BankAccount classes
...

# Creation and display of bank accounts
account1 = BankAccount("2023-01-01", customer1, 1000.0)
account2 = BankAccount("2023-01-02", customer2, 2000.0)

print(account1.username)
print(account2.username)
print(count1 == count2)

# Total balance display
print(BankAccount.total_balance())
```
## Example of expected output
```python
Account ID1: Example XYZ12301012023
Account identifier2: Example ABC12302012023
Are the two accounts equal? False
Total account balance: 3000.0
```
# Exercise 4 - Movie Class and Film Management

## Description

This exercise involves creating a `Movie` class to manage a collection of movies. This class will handle movie information and interact with a JSON file to store this data.

## Goals

1. **`Movie` class**:
    - Attributes: title (string), release date (string in DD/MM/YYYY format), and summary (string).
    - Creation of a JSON file in a `data` folder during the first instance of `Movie`, if this file does not exist.
    - Added new instances of `Movie` to the JSON file.
    - Method to remove a movie from the list in JSON file.
    - Methods to change the title, release date or summary of a movie.
    - Method to display information about a movie from its title.

2. **Terminal Application**:
    - `create` functionality to add a new movie.
    - `read` functionality to read information of a specific movie or view all movies in ascending order of release date.
    - `update` functionality to modify the information of a film.
    - `delete` functionality to delete a movie.
    - Searches by movie title work regardless of case.
    - Movie titles are stored with a capital letter for each word.

## Code Example

```python
# Definition of Movie class and methods to handle JSON file
...

# Examples of using commands in the terminal application
# create, read, update, delete
...
```
##Example of expected output
```python
# After running a 'create' command
Complete list of films after addition: [...]

# After executing a 'read' command
Information of the film sought: [...]

# After executing an 'update' command
Film after modification: [...]

# After executing a 'delete' command
Complete list of films after deletion: [...]

{
     "movies": [
         {
             "title": "The Dark Knight",
             "release_date": "08/13/2008",
             "description": "In this new installment, Batman ups the ante in his war against crime. With the support of Police Lieutenant Jim Gordon and Gotham District Attorney Harvey Dent, Batman aims to eradicate the organized crime that is proliferating in the city. Their partnership is very effective but it will soon be disrupted by the chaos unleashed by an extraordinary criminal whom the citizens of Gotham know as the Joker."
         }
     ]
}
```
