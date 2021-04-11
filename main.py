import pandas as pd
class Movie: 
    def __init__(self, title, date, genre, rating, gross, inflated_gross):
        self.title = title
        self.date = date
        self.genre = genre 
        self.rating = rating 
        self.gross = gross
        self.inflated_gross = inflated_gross

def print_movies(start, finish, movies):
    for i in range(start, finish):
        print(movies[i].title, movies[i].date, movies[i].genre, movies[i].rating, movies[i].gross, movies[i].inflated_gross)    
            
movies = []
titles = pd.read_csv('disney_movies_total_gross.csv', usecols=[0])
dates = pd.read_csv('disney_movies_total_gross.csv', usecols=[1])
genres = pd.read_csv('disney_movies_total_gross.csv', usecols=[2])
ratings = pd.read_csv('disney_movies_total_gross.csv', usecols=[3])
gross = pd.read_csv('disney_movies_total_gross.csv', usecols=[4])
inflated_gross = pd.read_csv('disney_movies_total_gross.csv', usecols=[5])

for j in range(len(titles)):
    movies.append(Movie(
        titles['movie_title'][j],
        dates['release_date'][j],
        genres['genre'][j],
        ratings['mpaa_rating'][j],
        gross['total_gross'][j],
        inflated_gross['inflation_adjusted_gross'][j]
    ))

print_movies(0,20,movies)