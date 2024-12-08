from django.db import models


class CustomUser(models.Model):
    """Кастомизированная модель пользователя."""

    telegram_id = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    photo_url = models.CharField(max_length=200, blank=True, null=True)
    auth_date = models.CharField(max_length=200, blank=True, null=True)

    @staticmethod
    def get_or_create_user(data: dict):
        user, _ = CustomUser.objects.get_or_create(
            telegram_id=data.get("id"),
            first_name=data.get("first_name", None),
            last_name=data.get("last_name", None),
            username=data.get("username", None),
            photo_url=data.get("photo_url", None),
            auth_date=data.get("auth_date", None),
        )
        return user

    def __str__(self):
        return self.telegram_id
