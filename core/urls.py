from django.urls import path
from .views import MovieRecommandations

app_name = 'core'

urlpatterns = [
    path('movies/', MovieRecommandations.as_view(), name='movie'),
]
