from users import *


def greet(user: BaseUser) -> str:
    strategy = {
        RegularUser: lambda user: f"Hello {user.username}, password is {user.password}",
        AdminUser: lambda user: f"Hello Administrator {user.username}, password is {user.password}",
        SuperUser: lambda user: f"Hello SuperUser {user.username}, password is {user.password}"
    }
    return strategy.get(type(user))(user)


if __name__ == '__main__':
    regular_user = RegularUser(username="User1", email="user@example.com", password="TopSecret1")
    admin_user = AdminUser(username="Admin", email="administrator@example.com", password="TopSecretAdminPassword")
    super_admin = SuperUser(username="SuperArmin", email="super-administrator@example.com",
                            password="SuperAdministrator")
    print(greet(user=regular_user))
    print(greet(user=admin_user))
    print(greet(user=super_admin))
