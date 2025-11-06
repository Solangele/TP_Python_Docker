import pandas as pd
import os
import datetime
from models.Movie import Movie
from exceptions.invalid_age_limit_exception import Invalid_age_limit
from exceptions.invalid_genre_exception import Invalid_genre
from exceptions.invalid_title_exception import Invalid_title
from exceptions.invalid_year_exception import Invalid_year


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'data', 'movies.csv')


def add_movie():
    current_year = datetime.datetime.now().year
    new_movie = None
    
    try :
        title = str(input("Saisisser le titre du film :"))
        if title.isdigit():
            raise Invalid_title("Le titre saisie est incorrect")
        
        year = int(input("Saisissez l'année de production :"))
        if year <= 1900 or year > current_year:
            raise Invalid_year("L'année de production saisie est incorrecte")
        
        genre = str(input("Saisissez le genre du film :"))
        if genre.isdigit():
            raise Invalid_genre("Le genre saisi est incorrect")
        
        age = int(input("Saisissez l'âge limite du film :"))
        if age <0 or age > 18 :
            raise Invalid_age_limit("L'âge saisi est incorrect")

    except (Invalid_title, Invalid_year, Invalid_genre, Invalid_age_limit) as e:
        print(e)

    else:
        print("Saisie correcte !")
        new_movie = Movie(Movie.id, title, year, genre, age)
        global df
        df = pd.concat([df, pd.DataFrame([new_movie.__dict__])], ignore_index=True)
        df.to_csv(CSV_PATH, index=False)
        
    finally:
        print("Fin de l'ajout !")


    return new_movie


def update_movie():
    current_year = datetime.datetime.now().year
    movie_id = int(input("Saisissez l'id du film à modifier :"))
    if movie_id in df['id'].values:
        try :
            title = str(input("Saisisser le titre du film :"))
            if title.isdigit():
                raise Invalid_title("Le titre saisie est incorrect")
        
            year = int(input("Saisissez l'année de production :"))
            if year <= 1900 or year > current_year:
                raise Invalid_year("L'année de production saisie est incorrecte")
            
            genre = str(input("Saisissez le genre du film :"))
            if genre.isdigit():
                raise Invalid_genre("Le genre saisi est incorrect")
            
            age = int(input("Saisissez l'âge limite du film :"))
            if age <0 or age > 18 :
                raise Invalid_age_limit("L'âge saisi est incorrect")

        except (Invalid_title, Invalid_year, Invalid_genre, Invalid_age_limit) as e:
            print(e)

        else:
            print("Saisie correcte !")
            df.loc[df['id'] == movie_id, ['title','year','genre','age']] = [title, year, genre, age]
            df.to_csv(CSV_PATH, index=False)
            return df[df['id'] == movie_id].iloc[0] 

        finally:
            print("Fin de l'ajout !")
    
    else : 
        print("Id non trouvé !")


def delete_movie():
    global df
    try:
        movie_id = int(input("Saisissez l'id du film à modifier :"))
        if movie_id in df['id'].values:
            validation = input(f"Voulez-vous vraiment supprimer le film {movie_id} ? (Y/N) : ")

            if validation.upper() == "N" :
                print("Le film n'a pas été supprimé !")
                return None

            elif validation.upper() == "Y" :
                df = df[df['id'] != movie_id]
                print(f"Le film {movie_id} a été supprimé.")

            else : 
                print("Saisie invalide !")
                return None
        
        else:
                print("Aucun film avec cet ID n'a été trouvé.")
                return None
    
    except ValueError:
        print("Veuillez saisir un id existant dans la liste !")
        return None



if __name__ == "__main__":
    df = pd.read_csv(CSV_PATH, sep=',', encoding='utf-8')
    print(df.head())

    movie = add_movie()
    print("Nouveau film ajouté :", movie)
    movie = add_movie()
    if movie is not None:
        print("Film ajouté :", movie)
    else:
        print("Aucun film n'a été ajouté.")

    update = update_movie()
    print("Le film a été modifié :", update)

    removed = delete_movie()
    if removed is not None:
        print("Film supprimé :", removed)


