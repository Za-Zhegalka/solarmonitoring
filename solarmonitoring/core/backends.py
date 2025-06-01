from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db import models


class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Пробуем найти пользователя по username или email
            user = UserModel.objects.get(
                models.Q(username__iexact=username) |
                models.Q(email__iexact=username)
            )
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
        except UserModel.MultipleObjectsReturned:
            return None