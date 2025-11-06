import pandas as pd
import os
from models.Movie import Movie


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'data', 'movies.csv')


def add_movie():
    title = str(input("Saisisser le titre du film :"))
    year = int(input("Saisissez l'année de production :"))
    genre = str(input("Saisissez le genre du film :"))
    age = int(input("Saisissez l'âge limite du film :"))

    new_movie = Movie(Movie.id, title, year, genre, age)
    return new_movie




if __name__ == "__main__":
    df = pd.read_csv(CSV_PATH, sep=',', encoding='utf-8')
    print(df.head())

    movie = add_movie()
    print("Nouveau film ajouté :", movie)


