# Create a url mapping file specifically for the app
from django.urls import path
from . import views  # import the file from the same folder


# create a mapping between urls and functions
# path("january", views.january)  # this function will be executed only for january-url
# first argument is a url path, second argument is a function

urlpatterns = [
    path(route="", view=views.index, name="index"),  # /challenge/

    # mapping with a placeholder, this function will be executed for any url, that comes after challenges/
    path(route="<int:month>", view=views.monthly_challenge_by_number),
    path(route="<str:month>", view=views.monthly_challenge, name="month-challenge")  # named url
]


