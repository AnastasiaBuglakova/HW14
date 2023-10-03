import io
import json
import os
import unittest
from unittest.mock import patch

from json_ import load_users
from classes import User, Terminal


# class TestJsonForUsers(unittest.TestCase):



class TestUserClass(unittest.TestCase):
    # проверяю грузятся ли пользователи, т е длину выгружаемого объекта
    def setUp(self):
        self.test_log_name = 'dog'
        self.test_log_id = '000023'
        self.test_new_name = 'adam ant'
        self.test_new_id = '111111'
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(
                {
                    "5": [
                        [
                            "dog",
                            23
                        ]
                    ],
                    "3": [
                        [
                            "fedya",
                            347
                        ]
                    ]
                },
                f, indent=6, ensure_ascii=False)

    def test_load_json_len(self):
        rer = load_users()
        self.assertEqual(len(rer), 2)


    def test_load_json_types(self):
        rer = load_users()
        self.assertIsInstance(rer.pop(), User)


    @patch("sys.stdout", new_callable=io.StringIO)
    def test_create_json_print_user1(self, mock_stdout):
        term = Terminal()
        term.users()
        self.assertIn('Имя: dog (000023 | Уровень доступа: 5)', mock_stdout.getvalue(),
                      'Тестовый пользователь 1 есть в выводе +')


    @patch("sys.stdout", new_callable=io.StringIO)
    def test_create_json_print_user2(self, mock_stdout):
        term = Terminal()
        term.users()
        self.assertIn('Имя: fedya (000347 | Уровень доступа: 3)', mock_stdout.getvalue(),
                      'Тестовый пользователь 2 есть в выводе +')


    def test_user_creation(self):
        term = Terminal()
        lg_user = term.log_in(self.test_log_name, self.test_log_id)
        term.create_new_user(lg_user, User(self.test_new_name, self.test_new_id, 5))
        self.assertIn(User('adam ant', '111111', 5), term.users_db(), "Pегистрация нового пользователя +")

    def test_log_in(self):
        term = Terminal()
        self.assertEqual(term.log_in(self.test_log_name, self.test_log_id), User('dog', '000023', 5), "Логирование тестового пользователя +")

    def tearDown(self) -> None:
        from pathlib import Path
        Path('users.json').unlink()



if __name__ == '__main__':
    print(os.getcwd())
    unittest.main()
