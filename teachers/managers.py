from django.contrib.auth.models import BaseUserManager


class UserCustomManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("User must have a username")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
