import unittest
import os
import sys
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from dataset import data_store, User
from werkzeug.security import generate_password_hash

class WorkflowIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

        data_store.reset_data()

        # Seed Doctor & Patient Users & Records
        doc_user = User(98, 'Dr. Smith', 'drsmith@test.com', '1234567890', 'Doctor', generate_password_hash('doc123'))
        pat_user = User(99, 'John Doe', 'johndoe@test.com', '9876543210', 'Patient', generate_password_hash('pat123'))
        data_store.users.extend([doc_user, pat_user])

        doctor = {'id': 98, 'doctor_name': 'Dr. Smith', 'specialization': 'Physician', 'qualification': 'MBBS', 'department': 'General Medicine', 'phone_number': '1234567890', 'email_address': 'drsmith@test.com', 'available_time': '09:00 - 17:00'}
        data_store.doctors.append(doctor)

        patient = data_store.add_patient({
            'full_name': 'John Doe', 'age': 32, 'gender': 'Male',
            'phone_number': '9876543210', 'email': 'johndoe@test.com',
            'address': '123 Main St', 'blood_group': 'B+', 'aadhaar_number': '500150015001'
        })

        self.doc_id = doctor['id']
        self.pat_id = patient['id']

    def test_complete_end_to_end_patient_workflow(self):
        # 1. Login as Doctor
        login_res = self.client.post('/', data={'email': 'drsmith@test.com', 'password': 'doc123', 'role': 'Doctor'}, follow_redirects=True)
        self.assertEqual(login_res.status_code, 200)

        # 2. Step 1: Schedule Appointment
        app_rec = data_store.add_appointment(self.pat_id, self.doc_id, datetime.date.today(), datetime.time(10, 0))
        self.assertIsNotNone(app_rec)

        # 3. Step 2 & 3: Save Consultation (Triggers Automated Workflow: Appointment Completion, EHR Diagnosis, Prescription, Notification)
        save_res = self.client.post('/api/consultations/save', json={
            'patient_id': self.pat_id,
            'patient_name': 'John Doe',
            'doctor_name': 'Dr. Smith',
            'consultation_date': '10-08-2026',
            'symptoms': 'Fever and Cough',
            'diagnosis': 'Viral Bronchitis',
            'treatment_prescription': 'Paracetamol 500mg, Cough Syrup'
        })
        self.assertEqual(save_res.status_code, 200)

        # Verify automated workflow results
        updated_app = next((a for a in data_store.appointments if a['id'] == app_rec['id']), None)
        self.assertEqual(updated_app['status'], 'Completed')

        consultations = data_store.get_consultations_by_patient(self.pat_id)
        self.assertTrue(len(consultations) > 0)

        prescriptions = data_store.get_prescriptions_by_patient(self.pat_id)
        self.assertTrue(len(prescriptions) > 0)

        # 4. Step 4: Generate Bill
        bill = data_store.create_bill(self.pat_id, 500.0, 200.0, 150.0, 0.0, 0.0, 'Cash', 'Paid')
        self.assertIsNotNone(bill)
        self.assertEqual(bill['total_amount'], 1003.0)

if __name__ == '__main__':
    unittest.main()
