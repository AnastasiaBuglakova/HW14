class UserException(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg


class LevelError(UserException):
    def __init__(self, log_level: int, new_level: int):
        super().__init__(f'Ошибка уровня доступа! Ваш уровень ({log_level}) меньше требуемого для создания пользователя уровня {new_level}')


class AccessError(UserException):
    def __init__(self, msg = ''):
        self.msg = "Ошибка доступа!" + ' ' + msg
        super().__init__(self.msg)

class NameAccessError(AccessError):
    def __init__(self, name):
        self.msg = f'Пользователя с имеменем "{name}" нет в БД'
        super().__init__(self.msg)


class IDAccessError(AccessError):
    def __init__(self, name, u_id):
        self.msg = f'Имя "{name}" не совпадает с айди в БД "{u_id}"'
        super().__init__(self.msg)



