from turtle import title
from core.models import Movie
import pandas as pd


def run():
    Movie.objects.all().delete()

    df = pd.read_csv('data.csv')
    i = 0
    for index, row in df.iterrows():
        try:
            movie = Movie.objects.create(
                id=i,
                img_url=row['img_url'],
                title=row['title'],
                year=row['year'],
                certificate=row['certificate'],
                duration=row['duration'],
                genre=row['genre'],
                imdb=row['imdb'],
                metascore=row['metascore'],
                overview=row['overview'],
                director=row['director'],
                actors=row['actors'],
            )
        except:
            movie = Movie.objects.create(
                id=i,
                img_url=row['img_url'],
                title=row['title'],
                year=2000,
                certificate=row['certificate'],
                duration=row['duration'],
                genre=row['genre'],
                imdb=row['imdb'],
                metascore=row['metascore'],
                overview=row['overview'],
                director=row['director'],
                actors=row['actors'],
            )
        i += 1
        movie.save()
