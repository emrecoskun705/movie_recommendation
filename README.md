
# Movie Recommendation

In this project I use Python Django Framework for creating backend side of my movie recommendation system.


## API Usage

#### Recommends movies using a movie(id)

```http
  GET /movies/{id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Required**. Give movie id for recommendation. |

#### Search movie

```http
  GET /search/{tag}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `tag`      | `string` | **Required**. Searchs by tag name in movie titles. |


## Start 

Python 3 or greater must be installed

```python 
git clone https://github.com/emrecoskun705/movie_recommendation.git
cd ./movie_recommendation
pip install ./requriments.txt 
python manage.py runserver
```


## Related Projects

[Mobile App](https://github.com/emrecoskun705/movie_recommendation_mobile)




  
