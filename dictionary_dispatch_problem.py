
from users import *

def greet(user: BaseUser)->None:
    strategy = {
        RegularUser: lambda user: f"Hello {user.username}, password is {user.password}",
        AdminUser: lambda user: f"Hello Administrator {user.username}, password is {user.password}",
    }

    default = lambda user:"I don't know how to handle this input"
    welcome_message = strategy.get(type(user), default)(user)
    print(welcome_message)


if __name__ == '__main__':
    regular_user = RegularUser(username="User1", email="user@example.com", password="TopSecret1")
    admin_user = AdminUser(username="Admin", email="administrator@example.com", password="TopSecretAdminPassword")
    super_admin = SuperUser(username="SuperArmin", email="super-administrator@example.com",
                            password="SuperAdministrator")

    greet(user=regular_user)
    greet(user=admin_user)
    greet(user=super_admin)