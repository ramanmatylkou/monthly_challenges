from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound  # import Django class for handling the http responses
from django.http import HttpResponseRedirect  # redirect function
from django.urls import reverse

# Create your views here.
# This views will be mapped to urls

all_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes a day!",
    "april": "Read one book",
    "may": "Learn new technology",
    "june": "Run every day",
    "july": "Visit a music concert",
    "august": "Go to a holiday",
    "september": "Come up with a new idea every day",
    "october": "Develop a game",
    "november": "Write an essay",
    "december": "Buy gifts!"
}


def index(request):
    list_items = ""
    months = list(all_challenges.keys())

    for month in months:
        month_path = reverse(viewname="month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def monthly_challenge(request, month: str):
    try:
        challenge_text = all_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"

        return HttpResponse(response_data)  # instantiate a response class
    except KeyError:
        return HttpResponseNotFound("This month is not supported!")


def monthly_challenge_by_number(request, month: int):
    all_months = list(all_challenges.keys())

    try:
        redirect_month = all_months[month - 1]

        # constructs an url like /challenges/january, by using named url
        redirect_path = reverse(viewname="month-challenge", args=[redirect_month])

        return HttpResponseRedirect(redirect_path)  # implement a redirect
    except IndexError:
        return HttpResponseNotFound("This month is not supported!")
