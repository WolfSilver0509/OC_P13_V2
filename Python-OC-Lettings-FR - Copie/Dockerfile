# Utilisation d'une image Python officielle en tant qu'image de base
FROM python:3.11

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie du fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Copie du fichier. env pour les variables secretes
COPY .env.docker .env

# Installation des dépendances Python
RUN pip install -r requirements.txt

# Copie du reste du code source dans le conteneur
COPY . .docker

# Exposition du port sur lequel l'application Django écoute
EXPOSE 8000

# Commande pour exécuter l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
