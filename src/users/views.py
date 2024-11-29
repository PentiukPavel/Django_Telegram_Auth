from django.shortcuts import render

from users.utils import HashCheck


def welcome(request):
    return render(request, "welcome.html")


def registry(request):
    if not HashCheck(request.GET).check_hash():
        error = "Данные не прошли проверку!"
        return render(request, "error.html", {"error": error})
