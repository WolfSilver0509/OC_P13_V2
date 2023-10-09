Base de données et structure des modèles
----------------------------------------


Base de données SQLite3
----------------------

SQLite est une bibliothèque C qui fournit une base de données légère basée sur le disque qui ne nécessite pas un processus de serveur séparé et permet d'accéder à la base de données en utilisant une variante non standard du langage de requête SQL. Il s'agit d'une base de données SQL autonome, basée sur des fichiers.
En tant que tel, nous n'avons pas besoin d'installer de modules ou de logiciels supplémentaires au fur et à mesure qu'il est fourni avec Python, et Django l'utilise nativement lors de la création d'un nouveau projet.

Contenu de la base de données
-----------------------------

Il y a 3 objets principaux dans la base de données:

Profile
Profils des utilisateurs/clients.
Chaque profil a un id (non affiché), un favori-city et un utilisateur-id (non affiché).
Un profil affiche certaines des informations de l'utilisateur stockées dans la table « utilisateur d'auth-utilisateur » : prénom, nom, adresse électronique et ville préférée.

Letting
Propriétés Listed où leur titre correspondant est affiché.
Chaque letting a un id (non affiché), un titre, et est lié à une adresse-id (non affichée, voir ci-dessous).

Adresse
Adresses de chaque bien.
Une adresse a un id (non affiché), un numéro, une rue, une ville, un état, un code postal et un code ISO de pays.


