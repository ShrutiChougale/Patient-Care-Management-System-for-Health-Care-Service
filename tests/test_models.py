import unittest
import os
import sys
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataset import data_store, User

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        data_store.reset_data()

    def test_user_password_hashing(self):
        u = User(99, 'Test User', 'test@example.com', '1234567890', 'Doctor')
        u.set_password('securepass123')
        data_store.users.append(u)

        retrieved_u = data_store.get_user_by_email('test@example.com')
        self.assertIsNotNone(retrieved_u)
        self.assertTrue(retrieved_u.check_password('securepass123'))
        self.assertFalse(retrieved_u.check_password('wrongpass'))

    def test_patient_creation_and_relationships(self):
        p = data_store.add_patient({
            'full_name': 'Test Patient',
            'age': 40,
            'gender': 'Male',
            'phone_number': '9999999999',
            'email': 'patienttest@example.com',
            'address': '123 Test St',
            'blood_group': 'O+',
            'aadhaar_number': '999988887777'
        })

        retrieved = data_store.get_patient_by_aadhaar('999988887777')
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved['full_name'], 'Test Patient')
        self.assertEqual(retrieved['aadhaar_number'], '999988887777')
        self.assertEqual(retrieved['masked_aadhaar'], 'XXXX-XXXX-7777')

    def test_aadhaar_validation_and_uniqueness(self):
        # 1. Invalid Aadhaar length should raise ValueError
        with self.assertRaises(ValueError):
            data_store.validate_aadhaar('123456') # Too short

        # 2. Duplicate Aadhaar
        p1 = data_store.add_patient({
            'full_name': 'User One', 'age': 25, 'gender': 'Male',
            'phone_number': '8888888882', 'email': 'u1@example.com', 'address': 'Test', 'blood_group': 'B+',
            'aadhaar_number': '987654321099'
        })
        self.assertIsNotNone(p1)

        with self.assertRaises(ValueError):
            data_store.add_patient({
                'full_name': 'User Two', 'age': 29, 'gender': 'Female',
                'phone_number': '8888888883', 'email': 'u2@example.com', 'address': 'Test', 'blood_group': 'AB+',
                'aadhaar_number': '987654321099' # Duplicate!
            })

    def test_medicine_inventory_and_feedback(self):
        today = datetime.date.today()
        m = data_store.add_medicine({
            'name': 'Test Medicine',
            'manufacturer': 'Test Lab',
            'category': 'Analgesics',
            'batch_number': 'BAT-01',
            'mfg_date': today,
            'exp_date': today,
            'price': 15.5,
            'stock': 100
        })

        all_meds = data_store.get_all_medicines()
        retrieved_m = next((item for item in all_meds if item['name'] == 'Test Medicine'), None)
        self.assertIsNotNone(retrieved_m)
        self.assertEqual(retrieved_m['price'], 15.5)

if __name__ == '__main__':
    unittest.main()
