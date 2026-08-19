import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from dataset import data_store, User
from werkzeug.security import generate_password_hash

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

        data_store.reset_data()

        # Seed Admin and Patient Users
        admin = User(98, 'Admin User', 'admin@test.com', '1111111111', 'Admin', generate_password_hash('admin123'))
        patient = User(99, 'Patient User', 'patient@test.com', '2222222222', 'Patient', generate_password_hash('patient123'))
        data_store.users.extend([admin, patient])

    def test_login_success_and_logout(self):
        response = self.client.post('/', data={
            'email': 'admin@test.com',
            'password': 'admin123',
            'role': 'Admin'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        logout_res = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(logout_res.status_code, 200)

    def test_rbac_access_denied_for_restricted_route(self):
        # Login as Patient
        self.client.post('/', data={
            'email': 'patient@test.com',
            'password': 'patient123',
            'role': 'Patient'
        }, follow_redirects=True)

        # Attempt to access Doctor-only route /doctors
        response = self.client.get('/doctors')
        self.assertEqual(response.status_code, 403)

if __name__ == '__main__':
    unittest.main()
