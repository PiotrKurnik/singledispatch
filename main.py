from functools import singledispatch


class BaseUser:

    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password
        self._is_admin = None

    @property
    def is_admin(self):
        return self._is_admin

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return "*"* len(self._password)

class RegularUser(BaseUser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._is_admin = False


class AdminUser(BaseUser):

    def __init__(self, *args, **kwargs):
        super(AdminUser, self).__init__(*args, **kwargs)
        self._is_admin = True

class SuperUser(AdminUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

@singledispatch
def greet_user():
    raise TypeError("Unkonw user!")

@greet_user.register(RegularUser)
def _(user):
    return f"Hello {user.username}, password is {user.password}"

@greet_user.register(AdminUser)
def _(user):
    return f"Hello Administrator {user.username}, password is {user.password}"

@greet_user.register(SuperUser)
def _(user):
    return f"Hello SuperUser {user.username}, password is {user.password}"


if __name__ == '__main__':
    regular_user = RegularUser(username="User1", email="user@example.com", password="TopSecret1")
    admin_user = AdminUser(username="Admin", email="administrator@example.com", password="TopSecretAdminPassword")
    super_admin = SuperUser(username="SuperArmin", email="super-administrator@example.com", password="SuperAdministrator")

    print(greet_user(regular_user))
    print(greet_user(admin_user))
    print(greet_user(super_admin))