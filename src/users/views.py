from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse

from users.models import CustomUser
from users.utils import HashCheck


def welcome(request):
    context = {
        "domain": settings.DOMAIN,
        "bot_name": settings.BOT_NAME,
    }
    return render(request, "welcome.html", context)


def registry(request):
    if not request.GET.get("hash", None):
        error = "Пройдите регистрацию"
        return render(request, "error.html", {"error": error})

    if not HashCheck(request.GET).check_hash():
        error = "Данные не прошли проверку!"
        return render(request, "error.html", {"error": error})

    user = CustomUser.get_or_create_user(request.GET)
    user.save()
    request.session["user_id"] = user.id
    return redirect(reverse("users:user_info"))


def user_info(request):
    user_id = request.session.get("user_id", None)
    if not user_id:
        return redirect(reverse("users:welcome"))
    user: CustomUser = CustomUser.objects.get(user_id)
    context = {"first_name": user.first_name, "last_name": user.last_name}
    return render(request, "user_info.html", context)
