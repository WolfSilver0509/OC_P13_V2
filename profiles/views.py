from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Affiche la liste des profils d'utilisateurs.

    Cette vue récupère tous les profils d'utilisateurs à partir de la base de données
    et les passe au modèle de template 'profiles/index.html' pour affichage.

    Pour afficher la liste des profils d'utilisateurs, appelez cette vue en utilisant
    la route '/profiles/' dans votre application Django.

    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Affiche le profil d'un utilisateur spécifique.

    Cette vue récupère le profil d'un utilisateur spécifique à partir de la base de données
    en fonction de son nom d'utilisateur ('username') et le passe au modèle de template
    'profiles/profile.html' pour affichage.

    Pour afficher le profil d'un utilisateur spécifique, appelez cette vue en utilisant
    une route qui inclut le nom d'utilisateur comme paramètre, par exemple,
    '/profiles/johndoe/'.

    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
