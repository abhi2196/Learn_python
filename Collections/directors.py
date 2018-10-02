import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors = defaultdict(list)
    with open(MOVIE_DATA, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = line['title_year']
                score = line['imdb_score']
            except ValueError:
                continue
            
            m = Movie(movie, year, score)
            directors[director].append(m)
            
    return directors


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    total_score = 0
    for movie in movies:
       total_score += float(movie.score) 
    return round(total_score / len(movies), 1)  


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    directors_list = list()
    Director = namedtuple('Director', 'director average_score')
    for director, movies in directors.items():
       min_year_pass = True
       for  m in movies:
          if m.year <= str(MIN_YEAR):
             min_year_pass = False 
       if len(movies) >= MIN_MOVIES and min_year_pass:
          avg_score = calc_mean_score(movies)
          d = Director(director, avg_score) 
          directors_list.append(d)
    directors_list.sort(key=lambda x:x[1], reverse=True)  
    return directors_list 
