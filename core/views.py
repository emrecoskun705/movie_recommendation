from rest_framework import generics
from .recommend import give_recommendations
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer


class MovieRecommandations(generics.ListAPIView):
    serializer_class = MovieSerializer
    lookup_url_kwarg = "id"

    def get_queryset(self):

        id = self.kwargs.get(self.lookup_url_kwarg)
        recommandation_list = give_recommendations(int(id))

        return Movie.objects.filter(pk__in=recommandation_list)


class MovieSearch(generics.ListAPIView):
    serializer_class = MovieSerializer
    lookup_url_kwarg = "tag"

    def get_queryset(self):
        tag = self.kwargs.get(self.lookup_url_kwarg)

        return Movie.objects.filter(title__contains=tag)[:10]
