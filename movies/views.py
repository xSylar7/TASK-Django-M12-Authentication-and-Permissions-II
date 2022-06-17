from django.db import OperationalError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from movies import models


def get_movies(request: HttpRequest) -> HttpResponse:
    try:
        movies: list[models.Movie] = list(models.Movie.objects.all())
    except OperationalError:
        movies = []

    context = {
        "movies": movies,
    }
    return render(request, "movie_list.html", context)
