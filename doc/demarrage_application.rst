Démarrage du projet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**WARNING**:

N'oubliez pas quand dans un cas comme dans l'autre il vous faut crée un fichier .env à la racine de votre projet et y mettre les variables d'environnement suivantes:

.. code-block:: shell

   SECRET_KEY=your_secret_key
   DEBUG=your_debug
   DNS=DNS_FOR_SENTRY,

N'oubliez pas également de rajouter sur votre repository le fichier .env dans le .gitignore afin de ne pas exposer vos secret .

Et rajouter les dans les variables secretes , dans votre repository github dans settings > secrets > new repository secret .


**CLONING**:

Pour cloner le référentiel, créez d'abord un dossier où vous voulez qu'il soit installé. Ouvrez votre terminal , allez dans ce dossier (cd C:\yourpath\yourfolder\) et initialisez git en tapant `git init`.

Vous pouvez maintenant obtenir l'application en clonant le référentiel :

.. code-block:: shell

   git clone https://github.com/WolfSilver0509/OC_P13_V2.git

**TÉLÉCHARGEMENT**:

Allez sur https://github.com/WolfSilver0509/OC_P13_V2.git, cliquez sur le bouton vert « Code » et choisissez « Télécharger le zip ». Extrayez le fichier zip où vous voulez que l'application soit.

Créer un environnement virtuel et installer les dépendances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Une fois fais dans votre PC, par le biais de votre terminal, allez dans ce répertoire et créez un environnement virtuel:

.. code-block:: shell

   cd OpenClassrooms-Project-13
   python -m venv venv  - pour crée l'environnement virtuel pour le projet

Activation de l'environnement virtuel:

.. code-block:: shell

   venv/Scripts/activate

Installer les modules nécessaires:

.. code-block:: shell

   pip install -r requirements.txt

Démarrage rapide : Exécuter l'application
-------------------------------------------

**Démarrage de l'application par Python**:

Pour démarrer le serveur, dans votre terminal (vous devez être dans le dossier racine de l'application où se trouve “manage.py”):

.. code-block:: shell

   python manage.py runserver

Vous devriez recevoir un message similaire à celui-ci :

System check identified 3 issues (0 silenced).
October 09, 2023 - 18:51:53
Django version 4.2.6, using settings 'oc_lettings_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Ouvrez votre navigateur et connectez-vous sur l'url via http://127.0.0.1:8000/ ou http://localhost:8000/

Pour arrêter le serveur, appuyez sur CTRL-C dans le terminal.

**Démarrage de l'application via Docker**:

Vous pouvez démarrer l'application en utilisant un conteneur Docker. Pour ce faire, démarrez Docker (s'il ne fonctionne pas déjà en arrière-plan).

Téléchargez l'image en ouvrant le fichier batch « dogcker-pull-image.bat ». Saisissez votre nom d'utilisateur et votre mot de passe. Si vous pouviez vous connecter avec succès, on vous demandera si vous souhaitez télécharger l'image. Tapez «y», appuyez sur ENTER et attendez que l'image ait été téléchargée. Le programme vous déconnectera automatiquement une fois le téléchargement terminé.

Vous ne verrez PAS de nouveau fichier dans votre dossier. Au lieu de cela, l'image est automatiquement téléchargée dans le dossier correspondant d'un Docker et apparaîtra directement dans le logiciel Docker Desktop.

Pour voir l'image vous pouvez également taper dans le shell "docker images" cela vous montrera les images crée sur docker.

Revenez au logiciel Docker, sélectionnez l'onglet « Images », et vous devriez voir l'image fraîchement téléchargée nommée « glaxer / docker_oc_lettings » avec l'étiquette « latest ».

Cliquez sur le bouton "exécuter"  et dans les réglages optionnels, tapez "8000" dans l'onglet "Ports", puis cliquez sur "Exécuter".

Un nouveau conteneur est créé, et l'image est en cours d'exécution. Vous devriez voir des lignes similaires à celles ci-dessus et quelques choses sur le dossier /static/:


System check identified 3 issues (0 silenced).
October 09, 2023 - 18:51:53
Django version 4.2.6, using settings 'oc_lettings_site.settings'
Starting development server at http://0.0.0.0.0.0:8000/
...
2023-10-09 21:49:14 [09/Oct/2023 19:00:14) “GET /static/assets/img/logo.png HT/1.1” 200 27037

Ouvrez votre navigateur et connectez-vous à l'application via http://127.0.0.1:8000/ ou http://localhost:8000/

Une fois que vous avez terminé, vous pouvez soit appuyer sur le bouton d'arrêt (le carré), soit appuyer directement sur la poubelle, ce qui arrêtera la course et supprimera le conteneur actuel.
