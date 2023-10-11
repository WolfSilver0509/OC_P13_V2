CI/CD Pipeline
--------------

Déploiement :

Outils :
~~~~~~~
- Github action ( workflow.yml )
- Docker
- Docker hub
- Azure

Le déploiement de mon projet Django est un processus automatisé qui comprend plusieurs étapes essentielles pour garantir un déploiement réussi. Voici les points clés à prendre en compte :

Configuration Requise :

- GitHub Actions : Configurer un dossier .github dans le dépôt avec un fichier workflow.yml. Ce fichier contient des actions GitHub qui automatisent le processus de déploiement.
- Variables github secrets n'oubliez pas de rajouter vos variables secrets dans le repository github , celle que vous utiliser dans votre workflow.yml.
- Tests et Linting : Le workflow GitHub commence par l'exécution de tests et de linters pour garantir que le projet fonctionne correctement et suit les bonnes pratiques de codage (flake8).
- Docker Image : On créé un fichier Dockerfile dans le projet Django pour créer une image Docker de l'application. Cette image doit être construite conformément à des spécifications spécifiques, telles que le type d'image et la version de Python.
- Variables Chiffrées : On utilise des variables chiffrées, également connues sous le nom de "variables de l'environnement" ou "variables secrètes", stockées en ligne sur "variable secrete github". Ces variables contiennent des informations sensibles nécessaires pour la configuration de l'application, mais elles ne sont pas accessibles au public.

Étapes du Déploiement :

- GitHub Actions : Lorsqu'un push est effectué sur la branche "master" du dépôt GitHub, le workflow démarre automatiquement. Il commence par l'exécution de tests pour vérifier que le code est fonctionnel et qu'il n'y a pas d'erreurs.
- Linting : Ensuite, le workflow vérifie la qualité du code en exécutant un linter pour s'assurer que le code suit les normes de codage (flake8).
- Build et Push de l'Image Docker : Si les tests et le linting sont réussis, le workflow passe à la construction de l'image Docker à partir du Dockerfile du projet Django.
- Docker Hub : Cette image est ensuite poussée vers Docker Hub pour la rendre disponible en ligne.
- Azure App Service : On configure un service Azure App Service pour déployer l'application. Les paramètres requis, tels que le type de conteneur Docker, ont été correctement configurés.
- Webhook : Chaque fois qu'une nouvelle image est poussée vers Docker Hub, elle déclenche un webhook qui informe Azure de la disponibilité de la nouvelle image.
- Déploiement Automatique : Azure récupère automatiquement la nouvelle image Docker depuis Docker Hub et la déploie sur Azure App Service. Cette étape assure que l'application est toujours à jour avec la dernière version.

En résumé, le processus de déploiement automatique commence par des tests et du linting sur GitHub, puis construit et pousse une image Docker sur Docker Hub. Azure surveille Docker Hub grâce à un webhook et met à jour automatiquement l'application sur Azure App Service à chaque nouvelle version de l'image. Ce processus garantit que l'application Django est continuellement mise à jour et fonctionne correctement en production.

.. note::
   Assurez-vous d'avoir toutes les dépendances et les configurations nécessaires en place avant de lancer le déploiement.