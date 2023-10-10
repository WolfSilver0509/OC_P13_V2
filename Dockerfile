# Utilisez une image de base Python
FROM python:3.9

# Définissez les variables d'environnement directement dans le Dockerfile
ARG DEBUG
ARG SECRET_KEY
ARG DNS
ENV DEBUG=${DEBUG}
ENV SECRET_KEY=${SECRET_KEY}
ENV DNS=${DNS}

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le contenu du répertoire de votre projet Django dans le conteneur
COPY . .

COPY static /app/static

# Installez les dépendances
RUN pip install -r requirements.txt

# Exécutez les migrations et créez la base de données
RUN python manage.py migrate

# Permettez de prendre les fichiers statiques et de les déposer dans static files
RUN python manage.py collectstatic --noinput

# Exposez le port sur lequel l'application Django s'exécute
EXPOSE 8000

# Lancez l'application Django en utilisant des variables d'environnement
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
