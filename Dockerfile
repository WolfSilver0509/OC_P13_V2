# Utilisez une image de base Python
FROM python:3.9

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le contenu du répertoire de votre projet Django dans le conteneur
COPY  . .

COPY static /app/static

# Installez les dépendances
RUN pip install -r requirements.txt

# Exécutez les migrations et créez la base de données
RUN python manage.py migrate

# Permet de prendre les fichier statics et les déposer dans static files
Run python manage.py collectstatic --noinput


# Exposez le port sur lequel l'application Django s'exécute
EXPOSE 8000

# Lancez l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
