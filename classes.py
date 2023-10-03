import json
from exceptions import AccessError, LevelError, NameAccessError, IDAccessError
# from json_ import create_json
# import json_


class User:

    def __init__(self, name: str, u_id: str, lvl: int):
        self.name = name
        self.u_id = str(u_id).zfill(6)
        self.lvl = int(lvl)

    def __str__(self):
        return f'Имя: {self.name} ({self.u_id} | Уровень доступа: {self.lvl})'

    def __repr__(self):
        return f'User({self.name}, {self.u_id}, {self.lvl})'

    def __eq__(self, other):
        if not isinstance(other, User):
            raise TypeError
        return self.name == other.name and self.u_id == other.u_id

    def __hash__(self):
        return hash((self.name + self.u_id) * self.lvl)


class Terminal:

    def __init__(self):
        self.users_base = Terminal.users_db()

    @staticmethod
    def users_db():
        users_list = set()
        with open('users.json', 'r', encoding='utf-8') as file:
            data_users = json.load(file)
            # print(f'-------------> {data_users = }')
        for lvl, users in data_users.items():
            for user in users:
                name, u_id = user
                users_list.add(User(name, u_id, lvl))
        return users_list

    def log_in(self, name, u_id):
        log_user = User(name, u_id, 0)
        users_name = [u_name.name for u_name in self.users_base]
        if name in users_name:
            for cur_user in self.users_base:
                print(f'{log_user=} { cur_user=}')
                if cur_user == log_user:
                    return cur_user
            raise IDAccessError(name, u_id)
        raise NameAccessError(name)

    def create_new_user(self, log_user, new_user):
        if new_user.lvl < log_user.lvl:
            raise LevelError(log_user.lvl, new_user.lvl)
        user_dict = {}
        self.users_base.add(new_user)
        for user in self.users_base:
            if user.lvl in user_dict:
                user_dict[user.lvl].append([user.name, user.u_id])
            else:
                user_dict[user.lvl] = [[user.name, user.u_id]]
        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump(user_dict, file, indent=4, ensure_ascii=False)

    def users(self):
        for user in self.users_base:
            print(user)



if __name__ == "__main__":
    term = Terminal()
    lg_user = term.log_in('fall', '000666')
    print(lg_user)
    # new_us = User('kuku', '666', 1)
    # # new_us = User('adam ant', '11', 7)
    # term.create_new_user(lg_user, new_us)
    # print('all users now:')
    # term.users()
