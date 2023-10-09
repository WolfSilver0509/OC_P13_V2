# Mettez à l'échelle une application Django en utilisant
une architecture modulaire Archivée avant le 17 Juillet 2023


Projet n°13 de la formation développeur d'Application Python.

:lock: ## Introduction : Voici la liste des contraintes à réspecter pour ce projet  :

Cahier des charges:

* (1) Réduction de diverses dettes techniques sur le projet
* (2) Refonte de l'architecture modulaire
* (3) Pipeline CI/CD et le déploiement
* (4) Surveillance de l’application et suivi des erreurs via Sentry.


:pushpin: ## "Déploiement :


 :mag: #outils

 * Github action ( workflow.yml )
 * Docker
 * Docker hub
 * Azur


Le déploiement de mon projet django un processus automatisé qui comprend plusieurs étapes essentielles pour garantir un déploiement réussi. Pour que le déploiement fonctionne correctement, voici les points clés à prendre en compte :
 
:point_right: Configuration Requise :

* GitHub Actions : Configuré un dossier .github dans le dépôt avec un fichier workflow.yml. Ce fichier contient des actions GitHub qui automatisent le processus de déploiement.
* Tests et Linting : Le workflow GitHub commence par l'exécution de tests et de linters pour garantir que le projet fonctionne correctement et suit les bonnes pratiques de codage (flake8).
* Docker Image : On créé un fichier Dockerfile dans le projet Django pour créer une image Docker de l'application. Cette image doit être construite conformément à des spécifications spécifiques, telles que le type d'image et la version de Python.
* Variables Chiffrées :On utilise des variables chiffrées, également connues sous le nom de "variables de l'environnement" ou "variables secrètes", stockées en ligne sur "variable secrete github". Ces variables contiennent des informations sensibles nécessaires pour la configuration de l'application, mais elles ne sont pas accessibles au public.

:point_right: Étapes du Déploiement :

* GitHub Actions : Lorsqu'un push est effectué sur la branch "master" du dépôt GitHub, le workflow démarre automatiquement. Il commence par l'exécution de tests pour vérifier que le code est fonctionnel et qu'il n'y a pas d'erreurs.
* Linting : Ensuite, le workflow vérifie la qualité du code en exécutant un linter pour s'assurer que le code suit les normes de codage (flake8).
* Build et Push de l'Image Docker : Si les tests et le linting sont réussis, le workflow passe à la construction de l'image Docker à partir du Dockerfile du projet Django.
* Docker hub : Cette image est ensuite poussée vers Docker Hub pour la rendre disponible en ligne.
* Azure App Service : On configure un service Azure App Service pour déployer l'application. Les paramètres requis, tels que le type de conteneur Docker, ont été correctement configurés.
* Webhook : Chaque fois qu'une nouvelle image est poussée vers Docker Hub, elle déclenche un webhook qui informe Azure de la disponibilité de la nouvelle image.
* Déploiement Automatique : Azure récupère automatiquement la nouvelle image Docker depuis Docker Hub et la déploie sur Azure App Service. Cette étape assure que l'application est toujours à jour avec la dernière version.


:computer: En résumé, le processus de déploiement automatique commence par des tests et du linting sur GitHub, puis construit et pousse une image Docker sur Docker Hub. Azure surveille Docker Hub grâce à un webhook et met à jour automatiquement l'application sur Azure App Service à chaque nouvelle version de l'image. Ce processus garantit que l'application Django est continuellement mise à jour et fonctionne correctement en production. 



<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://azure.microsoft.com/en-in/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" alt="azure" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> </p>



-------------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------------------------
## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`
