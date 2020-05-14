"""TODO: 1. login page
         2. captacha
         3.search part
         4.actual page parsing
"""
import imdb
import webbrowser

def movie_id(title):
    ia = imdb.IMDb()
    movies = ia.search_movie(title)
    movie = movies[0]
    return movie.movieID

def cinama_link(id):
    return "https://30nama.kim/imdb/title/tt"+id

def process():
    title = input("What's the name of the movie  > ")
    if "exit" in title:
        global t
        t = False
    else:
        id = movie_id(title)
        link = cinama_link(id)
        chrome_path = '/usr/bin/google-chrome'
        webbrowser.get(chrome_path).open(link)
t = True
while t==True:
    process()
