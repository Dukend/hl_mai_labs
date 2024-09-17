import unittest
import requests


class TestUserAPI(unittest.TestCase):
    BASE_URL = "http://localhost:8080/api/users"

    def test_find_by_name(self):
        response = requests.get(
            f"{self.BASE_URL}/find_by_name?first_name=Egor&second_name=Kondratev")
        self.assertEqual(response.status_code, 200)

    def test_find_by_login(self):
        response = requests.get(f"{self.BASE_URL}/find_by_login?login=dukend")
        self.assertEqual(response.status_code, 200)

    def test_new_user(self):
        data = {
            "user_name": "dukend",
            "first_name": "Egor",
            "second_name": "Kondratev",
            "password": "jfh9743hf8"
        }
        response = requests.post(f"{self.BASE_URL}/new_user", json=data)
        self.assertEqual(response.status_code, 200)

    def test_user_info(self):
        response = requests.get(f"{self.BASE_URL}/user_info?id=1")
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        response = requests.delete(f"{self.BASE_URL}/delete?user_id=11")
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        data = {
            "first_name": "Egorwew"
        }
        response = requests.put(
            f"{self.BASE_URL}/update?user_id=11", json=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
