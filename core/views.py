from rest_framework import generics
from .recommend import give_recommendations
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer


class MovieRecommandations(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):

        id = self.request.data['id']
        recommandation_list = give_recommendations(int(id))

        return Movie.objects.filter(pk__in=recommandation_list)
