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

#cover_title()



def cover_age():
    age= int(input("Saisir la limite d'âge souhaitée :"))
    filtered = data[data['age_limite'] == age]

    if not filtered.empty:
        print(filtered.to_string(index=False))
    else:
        print("Aucun film trouvé avec cet âge.")

#cover_age()


def type_movie():
    type = input("Saisir un genre de film:")
    filtered = data[data['genre'].str.lower() == type.lower()]

    if not filtered.empty:
        print(filtered.to_string(index=False))
    else:
        print("Aucun film de ce genre n'a été trouvé.")

type_movie()
