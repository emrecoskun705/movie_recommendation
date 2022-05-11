from django.urls import path
from .views import MovieRecommandations, MovieSearch

app_name = 'core'

urlpatterns = [
    path('movies/<int:id>', MovieRecommandations.as_view(), name='movie'),
    path('search/<str:tag>', MovieSearch.as_view(), name='search'),
]
