
class BaseUser:

    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password
        self._is_admin = False
        self._is_super_user = False

    @property
    def is_admin(self):
        return self._is_admin

    @property
    def is_super_user(self):
        return self._is_super_user

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
        self._is_super_user = True