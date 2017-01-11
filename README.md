***noovo-cli*** est une application en ligne de commande permettant d'obtenir le stream M3U8 des emmisions disponible sur Noovo.ca. Le stream peut être lu directement avec plusieurs lecteurs vidéos (VLC, SMPlayer, MPlayer, etc.).

Le projet est indépendant et n'est pas affilié à Noovo.ca.

### Dépendances

noovo-cli requiert : 
* Python 3, avec :
	* [Requests](http://python-requests.org/)	
	* [Simplejson](https://pypi.python.org/pypi/simplejson)	

### Installation

1. Installer les dépendances (le plus simple est d'utiliser pip).

	$ pip install NomDuPKG

2. Cloner le dépôt :

	$ git clone https://github.com/etiennedub/noovo-cli.git && cd noovo-cli

3. Exécuter ***noovo-cli***

	$ ./novoo-cli

Pour exécuter ***noovo-cli*** depuis n'importe quel répertoire :

	$ ln -s chemin/vers/dossier/bin/noovo-cli noovo-cli

### Utilisation
	noovo-cli [-h] [-v] [-sm] [-q [QUALITY]] [-u [URL]] [-l] [-a] [title] [episode]

	* title : Titre de l'émision
	* episode : Saison et épisode (ex.: s05e44)
	* -h, --help : Affiche l'aide
	* -v, --vlc : Lecture automatique avec VLC
	* -sm, --smplayer : Lecture automatique avec SMPlayer
	* -q [QUALITY], --quality [QUALITY] : Qualité de l'épisode (MIN, AVG, MAX, ALL)
	* -u [URL], --url [URL] : Sélectionner épisode à partir d'un URL Noovo.ca
	* -l, --last : Sélectionne le dernier épisode
	* -a, --audio : Audio seulement

**Exemple :** 

	$ noovo-cli "Un souper presque parfait" -v -l

Pour visionner la dernière épisode de *Un souper presque parfait* avec VLC.
