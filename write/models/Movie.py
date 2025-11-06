class Movie() :
    id = 31
    def __init__(self, titre, annee_production, genre, age_limite):
        
        self.titre = titre
        self.annee_production = annee_production
        self.genre = genre
        self.age_limite = age_limite
        Movie.id+=1
        self.id = Movie.id

    def __str__(self):
        return f"{self.titre},{self.annee_production},{self.genre},{self.age_limite}"
    
