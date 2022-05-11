from django.db import models

CERTIFICATE_CHOICES = (
    (0, "Young"),
    (1, "Kid"),
    (2, "General"),
    (3, "Adult"),
)


class Genre():
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    img_url = models.CharField(max_length=2000)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    certificate = models.IntegerField(
        choices=CERTIFICATE_CHOICES,
        null=True,
        blank=True,
    )
    duration = models.IntegerField()
    genre = models.CharField(max_length=150)
    imdb = models.FloatField()
    metascore = models.FloatField(null=True, blank=True)
    overview = models.CharField(max_length=10000)
    director = models.CharField(max_length=150)
    actors = models.CharField(max_length=600)

    def __str__(self):
        return self.title
