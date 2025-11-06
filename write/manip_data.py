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
    df = pd.read_csv(CSV_PATH, sep=',', encoding='utf-8')
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
        new_movie = Movie(title, year, genre, age)
        df = pd.concat([df, pd.DataFrame([new_movie.__dict__])], ignore_index=True)
        df.to_csv(CSV_PATH, index=False)
        
    finally:
        print("Fin de l'ajout !")


    return new_movie


def update_movie():
    df = pd.read_csv(CSV_PATH, sep=',', encoding='utf-8')
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
    df = pd.read_csv(CSV_PATH, sep=',', encoding='utf-8')
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
    
def display_movie():
    df = pd.read_csv(CSV_PATH, sep=',', encoding='utf-8')
    for _, row in df.iterrows():
        print(f"{int(row['id'])} {row['titre']} ({row['annee_production']}) {row['genre']} - Age: {row['age_limite']}")



def menu():
    while True:
        print("\n--- MENU ---")
        print("1 : Ajouter un film")
        print("2 : Modifier un film")
        print("3 : Supprimer un film")
        print("4 : Voir la liste des films")
        print("0 : Quitter")
        choice = input("Votre choix : ")

        match choice:
            case "1":
                add_movie()
            case "2":
                update_movie()
            case "3":
                delete_movie()
            case "4":
                display_movie()
            case "0":
                print("Au revoir !")
                break
            case _:
                print("Choix invalide, réessayez.")


menu()







