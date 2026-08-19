import unittest
import os
import sys
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from dataset import data_store, User
from werkzeug.security import generate_password_hash

class APITestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

        data_store.reset_data()
        u = User(99, 'API Admin', 'apiadmin@test.com', '1234567890', 'Admin', generate_password_hash('api123'))
        data_store.users.append(u)

    def test_jwt_auth_login_and_protected_endpoint(self):
        # 1. Login to get JWT Token
        login_res = self.client.post('/api/v1/auth/login', json={
            'email': 'apiadmin@test.com',
            'password': 'api123'
        })
        self.assertEqual(login_res.status_code, 200)
        data = login_res.get_json()
        self.assertTrue(data['success'])
        token = data['token']

        # 2. Access protected endpoint with JWT Header
        headers = {'Authorization': f'Bearer {token}'}
        patients_res = self.client.get('/api/v1/patients', headers=headers)
        self.assertEqual(patients_res.status_code, 200)

        # 3. Create Patient via API with Aadhaar Number
        create_res = self.client.post('/api/v1/patients', json={
            'full_name': 'REST API Patient',
            'phone_number': '8888888888',
            'age': 29,
            'gender': 'Female',
            'email': 'restpatient@test.com',
            'aadhaar_number': '555566667777'
        }, headers=headers)
        self.assertEqual(create_res.status_code, 201)

        # 4. Fetch Patient details by Aadhaar via API
        aadhaar_res = self.client.get('/api/v1/patients/aadhaar/555566667777', headers=headers)
        self.assertEqual(aadhaar_res.status_code, 200)
        aadhaar_data = aadhaar_res.get_json()
        self.assertTrue(aadhaar_data['success'])
        self.assertEqual(aadhaar_data['data']['masked_aadhaar'], 'XXXX-XXXX-7777')

if __name__ == '__main__':
    unittest.main()
