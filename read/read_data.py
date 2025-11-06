from models.Movie import Movie
import pandas as pd

data = pd.read_csv("read/data/movies.csv")
print(data)

def cover_title():
    title = input("Saisir un titre de film:")
    filtered = data[data['titre'].str.lower() == title.lower()]

    if not filtered.empty:
        print(filtered.to_string(index=False))
    else:
        print("Aucun film trouvé avec ce titre.")

cover_title()




