
Description de l'API
--------------------

L'API se compose de 4 applications :

1. Le site d'accueil, qui s'occupe de la section d'administration et relie les 3 autres applications ensemble.

2. Homeapp, qui gère la page principal d'index

3. Lettings, qui gère la page principale des locations ainsi que chaque page.

4. Profile, qui gère la page principale des profils ainsi que chaque page de profil individuel.

En cas d'erreur: Sentry
~~~~~~~~~~~~~~~~~~~~~~~~

Sentry a été mis en œuvre afin d'avertir l'administrateur en tout état de cause que des erreurs devaient se produire. Il est possible de renvoyer des erreurs personnalisées, ce qui a été fait en cas de « mauvaise demande » ou d'erreur 500. Cela se produit lorsque l'utilisateur entre une URL invalide qui cible un objet qui n'existe pas dans la base de données.
Les erreurs sont répertorier comme demander dans un projet sentry qui stock les divers erreurs fournis. Dans ce projet j'ai crée une url ( /sentry-debug )qui déclenche une erreur sentry afin de voir le bon déroulement pour capter des erreurs.