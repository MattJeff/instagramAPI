# ScriptHub

ScriptHub est une application SaaS qui permet d'extraire des scripts à partir de vidéos Instagram en utilisant simplement l'URL de la vidéo. Vous pouvez également organiser les scripts extraits dans des listes pour les consulter plus tard.

## Fonctionnalités

- Extraction de scripts vidéo à partir d'URL Instagram.
- Récupération des informations de la vidéo (date de publication, nombre de likes, commentaires, partages, etc.).
- Organisation des scripts extraits dans des listes personnalisées.

## Prérequis

- Python 3.8+
- `pip` (Python package installer)
- Un compte Instagram valide pour l'authentification

## Installation

1. Clonez le dépôt GitHub :

   ```bash
   git clone https://github.com/MattJeff/instagramAPI.git
   cd votre-depot

2. Créez et activez un environnement virtuel : 
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`

3. Installez les dépendances : 
   pip3 install -r requirements.txt

4. Créez un fichier .env dans le répertoire racine du projet et ajoutez vos identifiants Instagram : 
   INSTAGRAM_USERNAME=votre_nom_utilisateur_instagram
   INSTAGRAM_PASSWORD=votre_mot_de_passe_instagram

## Utilisation

1. Démarrez l'application Flask: 
   python run.py
 
2. L'application sera accessible sur http://127.0.0.1:5002 . Vous pouvez utiliser ngrok pour avoir un lien web exploitable. commande : ngrok 5002

3. Utilisez un outil comme Postman pour tester les endpoints
    Extraire le script d'une vidéo :

    URL : http://127.0.0.1:5002/get_script_video_url
    Méthode : POST
    Body (JSON) :

    Copier le code
    {
        "video_url": "URL de la vidéo Instagram"
    }

## Développement

Structure du Projet
    app/ : Contient le code principal de l'application Flask.
        __init__.py : Initialise l'application Flask.
        routes.py : Définit les routes/endpoints de l'application.
        utils.py : Contient les fonctions utilitaires pour l'extraction des scripts et des informations utilisateur.
    run.py : Script pour démarrer l'application Flask.
    requirements.txt : Liste des dépendances Python nécessaires.
    .env : Fichier pour les variables d'environnement (à créer).

## Contribution

    Les contributions sont les bienvenues ! Pour contribuer :
1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (git checkout -b ma-nouvelle-fonctionnalité).
3. Commitez vos changements (git commit -am 'Ajouter une nouvelle fonctionnalité').
4. Poussez votre branche (git push origin ma-nouvelle-fonctionnalité).
5. Ouvrez une Pull Request.

## License

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.


