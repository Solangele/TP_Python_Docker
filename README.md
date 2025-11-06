# TP_Python_Docker

## Récupération du projet sur git
```bash
git clone https://github.com/Solangele/TP_Python_Docker.git
```


## Lancement du projet sous Docker
Dans les Dockerfiles : 
Etant donné que j'ai utilisé Pandas, ne pas oublier le RUN pip install pandas. 

Dans le docker-compose.yml :
Utilisation de deux conteneurs, read et write.
Dans le conteneur read, utilisation des commandes : 
```bash
    build: ./read

    container_name: my-app-read

    restart: always

    volumes: 
      - data_volume:/data

    ports: 
      - 5000:5000

    networks:
      - app_network
```

Dans le conteneur write, utilisation des commandes : 
```bash
    build: ./write
    
    container_name: my-app-write
      
    restart: always

    ports: 
      - 5001:5000

    volumes: 
      - data_volume:/data

    networks:
      - app_network
```

Ensuite, dans Docker, il faut aller dans le chemin qui mène au dossier puis utiliser la commande : 
```bash
docker compose up -d
```

## Utilisation des applications
### Read
Dans le read, on peut filtrer les films :
    - par recherche du nom,
    - par limite d'âge,
    - par genre, 
    - dans un laps de temps, pour l'année de production. 

Je n'ai pas mis d'entrées valides ou invalides dans le read, il s'agit d'un axe d'amélioration à prévoir. 


### Write
Dans le write, on peut :
    - ajouter un film au csv,
    - modifier un film dans le csv,
    - supprimer un film qui est dans le csv.

Des messages d'erreurs apparaîssent si les entrées ne sont pas valides : 
    - si le titre n'est pas un string,
    - si la limite d'âge n'est pas un integer,
    - si le genre n'est pas un string,
    - si les années de production demandées ne sont pas des integer.

### Exemples d'utilisation
Pour le Write : 

--- MENU ---
1 : Ajouter un film
2 : Modifier un film
3 : Supprimer un film
4 : Voir la liste des films
0 : Quitter
Votre choix : 1
Saisisser le titre du film :Papaoutet
Saisissez l'année de production :2015
Saisissez le genre du film :Famille
Saisissez l'âge limite du film :6
Saisie correcte !
Fin de l'ajout !

31 Mamma mia (2016) Humour - Age: 12
32 jumanji (1995) Aventure - Age: 12
33 Papaoutet (2015) Famille - Age: 6


--- MENU ---
1 : Ajouter un film
2 : Modifier un film
3 : Supprimer un film
4 : Voir la liste des films
0 : Quitter
Votre choix : 2
Saisissez l'id du film à modifier :32
Saisisser le titre du film :Papaoutaaat
Saisissez l'année de production :2017
Saisissez le genre du film :Humour
Saisissez l'âge limite du film :12
Saisie correcte !

32 Papaoutaaat (2017) Humour - Age: 12


--- MENU ---
1 : Ajouter un film
2 : Modifier un film
3 : Supprimer un film
4 : Voir la liste des films
0 : Quitter
Votre choix : 3
Saisissez l'id du film à supprimer :32
Voulez-vous vraiment supprimer le film 32 ? (Y/N) : y
Le film 32 a été supprimé.

31 Mamma mia (2016) Humour - Age: 12
33 Papaoutet (2015) Famille - Age: 6



Pour le read : 
Saisir un titre de film:Avatar

 id  titre  annee_production  genre  age_limite
 27 Avatar              2009 Action          12



Saisir la limite d'âge souhaitée :3

 id                      titre  annee_production     genre  age_limite
 16              The Lion King              1994 Animation           3
 25 E.T. the Extra-Terrestrial              1982   Famille           3



Saisir un genre de film:Comédie

 id      titre  annee_production   genre  age_limite
 15   Parasite              2019 Comédie          16
 29 La La Land              2016 Comédie           6



Saisir l'année de production minimum :1998
Saisir l'année de production maximum :2002

 id                                             titre  annee_production     genre  age_limite
  7                                        The Matrix              1999    Action          16
 10                                        Fight Club              1999     Drame          18
 12 The Lord of the Rings: The Fellowship of the Ring              2001  Aventure          12
 14                                     Spirited Away              2001 Animation           6
 17                                         Gladiator              2000    Action          12
 20                               Saving Private Ryan              1998     Drame          16
