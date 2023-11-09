from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404  # import Django class for handling the http responses
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
    "december": None
}


def index(request):
    months = list(all_challenges.keys())
    return render(
        request=request,
        template_name="challenges/index.html",
        context={"months": months})


def monthly_challenge(request, month: str):
    try:
        challenge_text = all_challenges[month]

        # read html file and transform it to string, and return as http response
        return render(
            request=request,
            template_name="challenges/challenge.html",
            context={"month_name": month,
                     "text": challenge_text})
        # return HttpResponse(response_data)  # instantiate a response class

    except KeyError:
        raise Http404()  # this method automatically will find 404 template in the root folder
        # return HttpResponseNotFound("This month is not supported!")


def monthly_challenge_by_number(request, month: int):
    all_months = list(all_challenges.keys())

    try:
        redirect_month = all_months[month - 1]

        # constructs an url like /challenges/january, by using named url
        redirect_path = reverse(viewname="month-challenge", args=[redirect_month])

        return HttpResponseRedirect(redirect_path)  # implement a redirect
    except IndexError:
        raise Http404()
        # return HttpResponseNotFound("This month is not supported!")
