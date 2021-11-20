from functools import singledispatch

from users import *

@singledispatch
def greet_user(user):
    return f"I am the default action for {user.username}"

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