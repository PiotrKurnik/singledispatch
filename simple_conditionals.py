from users import *


def greet_user(user) -> str:
    if isinstance(user, RegularUser):
        return f"Hello {user.username}, password is {user.password}"
    elif isinstance(user, AdminUser):
        return f"Hello Administrator {user.username}, password is {user.password}"
    elif isinstance(user, SuperUser):
        return f"Hello SpeerUser {user.username}, password is {user.password}"
    else:
        return f"I am the default action for {user.username}"


if __name__ == '__main__':
    regular_user = RegularUser(username="User1", email="user@example.com", password="TopSecret1")
    admin_user = AdminUser(username="Admin", email="administrator@example.com", password="TopSecretAdminPassword")
    super_admin = SuperUser(username="SuperArmin", email="super-administrator@example.com",
                            password="SuperAdministrator")

    print(greet_user(regular_user))
    print(greet_user(admin_user))
    print(greet_user(super_admin))
