import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, '..', 'data', 'movies.csv')

class Movie() :
    id = None
    def __init__(self, titre, annee_production, genre, age_limite):
        
        self.titre = titre
        self.annee_production = annee_production
        self.genre = genre
        self.age_limite = age_limite
        if Movie.id is None:
            Movie.id = self._get_last_id_from_csv()
        Movie.id+=1
        self.id = Movie.id

    def _get_last_id_from_csv(self):
        """Récupère le dernier ID dans le CSV, ou 0 si le fichier est vide."""
        if not os.path.exists(CSV_PATH):
            return 0
        df = pd.read_csv(CSV_PATH)
        if df.empty:
            return 0
        return df['id'].max()


    def __str__(self):
        return f"{self.titre},{self.annee_production},{self.genre},{self.age_limite}"
    
