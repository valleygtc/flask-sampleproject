import unittest

from app import db, Student
from . import test_app


def fake_records(num):
    for i in range(num):
        s = Student(
            name=f'testStudent{i}',
            age=18,
            address='testAddress',
        )
        db.session.add(s)
    db.session.commit()


class TestIndex(unittest.TestCase):
    url = '/'

    def test_normal(self):
        client = test_app.test_client()
        resp = client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.get_data(as_text=True),
            'Hello, World!'
        )


class TestStudentShow(unittest.TestCase):
    url = '/students/'

    def setUp(self):
        with test_app.app_context():
            db.create_all()
            fake_records(5)
    
    def tearDown(self):
        with test_app.app_context():
            db.drop_all()

    def test_normal(self):
        client = test_app.test_client()
        resp = client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        json_data = resp.get_json()
        self.assertIn('data', json_data)


class TestStudentAdd(unittest.TestCase):
    url = '/students/add'

    data = {
        'name': 'fooName',
        'age': 18,
        'address': 'fooAddress',
    }

    def setUp(self):
        with test_app.app_context():
            db.create_all()
    
    def tearDown(self):
        with test_app.app_context():
            db.drop_all()

    def test_normal(self):
        client = test_app.test_client()
        body = self.data.copy()
        resp = client.post(self.url, json=body)
        self.assertEqual(resp.status_code, 200)
        json_data = resp.get_json()
        self.assertIn('msg', json_data)
        # 验证已插入数据库
        with test_app.app_context():
            self.assertTrue(Student.query.get(1))
    
    def test_lack_name(self):
        client = test_app.test_client()
        body = self.data.copy().pop('name')
        resp = client.post(self.url, json=body)
        self.assertEqual(resp.status_code, 400)
        json_data = resp.get_json()
        self.assertIn('msg', json_data)
