import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, id, full_name, email, phone_number, role, password_hash=None):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.role = role
        self.password_hash = password_hash or generate_password_hash('admin123')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class DataStore:
    def __init__(self):
        self.reset_data()

    def reset_data(self):
        # 1. Users (All Roles & Accounts)
        self.users = [
            User(1, 'System Admin', 'admin@gmail.com', '1234567890', 'Admin', generate_password_hash('admin123')),
            User(2, 'Dr. John Smith', 'doctor@gmail.com', '1234567891', 'Doctor', generate_password_hash('doctor123')),
            User(3, 'Dr. John Smith', 'drjohn@example.com', '9988776655', 'Doctor', generate_password_hash('doctor123')),
            User(4, 'Dr. Priya', 'drpriya@gmail.com', '9988776654', 'Doctor', generate_password_hash('doctor123')),
            User(5, 'Dr. Priya', 'drpriya@example.com', '9988776654', 'Doctor', generate_password_hash('doctor123')),
            User(6, 'Dr. Rajesh', 'drrajesh@example.com', '9988776653', 'Doctor', generate_password_hash('doctor123')),
            User(7, 'Nurse Test', 'nurse@gmail.com', '1234567892', 'Nurse', generate_password_hash('nurse123')),
            User(8, 'Pharm Pharmacist', 'pharmacist@gmail.com', '1234567893', 'Pharmacist', generate_password_hash('pharmacist123')),
            User(9, 'Lab Technician', 'lab@gmail.com', '1234567894', 'Laboratory Staff', generate_password_hash('lab123')),
            User(10, 'Rahul Kumar', 'patient@gmail.com', '9876543210', 'Patient', generate_password_hash('patient123')),
            User(11, 'Sneha Reddy', 'sneha@example.com', '9876543211', 'Patient', generate_password_hash('patient123')),
            User(12, 'Amit Verma', 'amit@example.com', '9876543212', 'Patient', generate_password_hash('patient123')),
            User(13, 'Pooja Sharma', 'pooja@example.com', '9876543213', 'Patient', generate_password_hash('patient123')),
            User(14, 'Vikram Malhotra', 'vikram@example.com', '9876543214', 'Patient', generate_password_hash('patient123')),
            User(15, 'Ananya Roy', 'ananya@example.com', '9876543215', 'Patient', generate_password_hash('patient123')),
            User(16, 'Suresh Nair', 'suresh@example.com', '9876543216', 'Patient', generate_password_hash('patient123')),
            User(17, 'Meera Kapoor', 'meera@example.com', '9876543217', 'Patient', generate_password_hash('patient123')),
            User(18, 'Rajesh Patel', 'rajesh@example.com', '9876543218', 'Patient', generate_password_hash('patient123')),
            User(19, 'Deepa Iyer', 'deepa@example.com', '9876543219', 'Patient', generate_password_hash('patient123'))
        ]

        # 2. Doctors
        self.doctors = [
            {'id': 1, 'doctor_name': 'Dr. John Smith', 'specialization': 'Cardiologist', 'qualification': 'MD Cardiology', 'department': 'Cardiology', 'phone_number': '9988776655', 'email_address': 'drjohn@example.com', 'available_time': '09:00 AM - 05:00 PM'},
            {'id': 2, 'doctor_name': 'Dr. Priya', 'specialization': 'Physician', 'qualification': 'MBBS, MD', 'department': 'General Medicine', 'phone_number': '9988776654', 'email_address': 'drpriya@example.com', 'available_time': '10:00 AM - 04:00 PM'},
            {'id': 3, 'doctor_name': 'Dr. Rajesh', 'specialization': 'Neurologist', 'qualification': 'DM Neurology', 'department': 'Neurology', 'phone_number': '9988776653', 'email_address': 'drrajesh@example.com', 'available_time': '11:00 AM - 06:00 PM'}
        ]

        # 3. 10 Distinct Patient Records (with unique 12-digit Aadhaar numbers)
        self.patients = [
            {'id': 1, 'patient_code': 'PAT1001', 'full_name': 'Rahul Kumar', 'age': 28, 'gender': 'Male', 'phone_number': '9876543210', 'email': 'patient@gmail.com', 'address': '123 Green Street, Chennai', 'blood_group': 'O+', 'aadhaar_number': '100000000001', 'date_of_birth': '15-05-1996', 'height': '175 cm', 'weight': '72 kg', 'bmi': '23.5', 'smoking': 'No', 'alcohol': 'Occasional', 'chronic_diseases': 'No', 'remarks': 'Patient is healthy.', 'medical_history': 'No prior surgical history.'},
            {'id': 2, 'patient_code': 'PAT1002', 'full_name': 'Sneha Reddy', 'age': 26, 'gender': 'Female', 'phone_number': '9876543211', 'email': 'sneha@example.com', 'address': '45 Park Avenue, Chennai', 'blood_group': 'A+', 'aadhaar_number': '100000000002', 'date_of_birth': '10-08-1998', 'height': '162 cm', 'weight': '58 kg', 'bmi': '22.1', 'smoking': 'No', 'alcohol': 'No', 'chronic_diseases': 'No', 'remarks': 'Good general health.', 'medical_history': 'Seasonal allergies.'},
            {'id': 3, 'patient_code': 'PAT1003', 'full_name': 'Amit Verma', 'age': 35, 'gender': 'Male', 'phone_number': '9876543212', 'email': 'amit@example.com', 'address': '88 Lake Road, Chennai', 'blood_group': 'B+', 'aadhaar_number': '100000000003', 'date_of_birth': '12-03-1989', 'height': '178 cm', 'weight': '78 kg', 'bmi': '24.6', 'smoking': 'No', 'alcohol': 'Social', 'chronic_diseases': 'Hypertension', 'remarks': 'Requires regular BP checkup.', 'medical_history': 'Diagnosed with Hypertension in 2024.'},
            {'id': 4, 'patient_code': 'PAT1004', 'full_name': 'Pooja Sharma', 'age': 31, 'gender': 'Female', 'phone_number': '9876543213', 'email': 'pooja@example.com', 'address': '12 MG Road, Chennai', 'blood_group': 'AB+', 'aadhaar_number': '100000000004', 'date_of_birth': '05-11-1993', 'height': '165 cm', 'weight': '60 kg', 'bmi': '22.0', 'smoking': 'No', 'alcohol': 'No', 'chronic_diseases': 'No', 'remarks': 'Under observation for gastritis.', 'medical_history': 'Gastritis flares.'},
            {'id': 5, 'patient_code': 'PAT1005', 'full_name': 'Vikram Malhotra', 'age': 42, 'gender': 'Male', 'phone_number': '9876543214', 'email': 'vikram@example.com', 'address': '102 Civil Lines, Delhi', 'blood_group': 'O-', 'aadhaar_number': '100000000005', 'date_of_birth': '20-01-1984', 'height': '180 cm', 'weight': '85 kg', 'bmi': '26.2', 'smoking': 'Yes', 'alcohol': 'Regular', 'chronic_diseases': 'Type-2 Diabetes', 'remarks': 'Insulin dosage under evaluation.', 'medical_history': 'Type-2 Diabetes since 2020.'},
            {'id': 6, 'patient_code': 'PAT1006', 'full_name': 'Ananya Roy', 'age': 24, 'gender': 'Female', 'phone_number': '9876543215', 'email': 'ananya@example.com', 'address': '77 Salt Lake, Kolkata', 'blood_group': 'A-', 'aadhaar_number': '100000000006', 'date_of_birth': '14-07-2000', 'height': '158 cm', 'weight': '52 kg', 'bmi': '20.8', 'smoking': 'No', 'alcohol': 'No', 'chronic_diseases': 'Asthma', 'remarks': 'Prescribed Inhaler.', 'medical_history': 'Mild persistent asthma.'},
            {'id': 7, 'patient_code': 'PAT1007', 'full_name': 'Suresh Nair', 'age': 50, 'gender': 'Male', 'phone_number': '9876543216', 'email': 'suresh@example.com', 'address': '19 Marine Drive, Mumbai', 'blood_group': 'B-', 'aadhaar_number': '100000000007', 'date_of_birth': '30-09-1974', 'height': '170 cm', 'weight': '75 kg', 'bmi': '25.9', 'smoking': 'No', 'alcohol': 'Social', 'chronic_diseases': 'High Cholesterol', 'remarks': 'Routine lipid monitoring.', 'medical_history': 'Hyperlipidemia.'},
            {'id': 8, 'patient_code': 'PAT1008', 'full_name': 'Meera Kapoor', 'age': 29, 'gender': 'Female', 'phone_number': '9876543217', 'email': 'meera@example.com', 'address': '55 Jubilee Hills, Hyderabad', 'blood_group': 'AB-', 'aadhaar_number': '100000000008', 'date_of_birth': '18-02-1995', 'height': '168 cm', 'weight': '64 kg', 'bmi': '22.7', 'smoking': 'No', 'alcohol': 'No', 'chronic_diseases': 'Thyroid Deficiency', 'remarks': 'Thyroxine 50mcg daily.', 'medical_history': 'Hypothyroidism.'},
            {'id': 9, 'patient_code': 'PAT1009', 'full_name': 'Rajesh Patel', 'age': 38, 'gender': 'Male', 'phone_number': '9876543218', 'email': 'rajesh@example.com', 'address': '14 SG Highway, Ahmedabad', 'blood_group': 'O+', 'aadhaar_number': '100000000009', 'date_of_birth': '09-04-1986', 'height': '172 cm', 'weight': '70 kg', 'bmi': '23.7', 'smoking': 'No', 'alcohol': 'No', 'chronic_diseases': 'No', 'remarks': 'Annual executive health checkup.', 'medical_history': 'None.'},
            {'id': 10, 'patient_code': 'PAT1010', 'full_name': 'Deepa Iyer', 'age': 33, 'gender': 'Female', 'phone_number': '9876543219', 'email': 'deepa@example.com', 'address': '90 Indiranagar, Bengaluru', 'blood_group': 'A+', 'aadhaar_number': '100000000010', 'date_of_birth': '25-12-1991', 'height': '160 cm', 'weight': '56 kg', 'bmi': '21.9', 'smoking': 'No', 'alcohol': 'Occasional', 'chronic_diseases': 'Migraine', 'remarks': 'Pain management consultation.', 'medical_history': 'Chronic migraine.'}
        ]

        # 4. Appointments
        self.appointments = [
            {'id': 1, 'patient_id': 1, 'doctor_id': 2, 'appointment_date': datetime.date.today(), 'appointment_time': datetime.time(10, 30), 'status': 'Completed'},
            {'id': 2, 'patient_id': 2, 'doctor_id': 1, 'appointment_date': datetime.date.today(), 'appointment_time': datetime.time(11, 00), 'status': 'Scheduled'},
            {'id': 3, 'patient_id': 3, 'doctor_id': 2, 'appointment_date': datetime.date.today(), 'appointment_time': datetime.time(11, 30), 'status': 'Completed'},
            {'id': 4, 'patient_id': 5, 'doctor_id': 3, 'appointment_date': datetime.date.today(), 'appointment_time': datetime.time(14, 00), 'status': 'Completed'},
            {'id': 5, 'patient_id': 7, 'doctor_id': 1, 'appointment_date': datetime.date.today(), 'appointment_time': datetime.time(15, 30), 'status': 'Scheduled'},
            {'id': 6, 'patient_id': 10, 'doctor_id': 3, 'appointment_date': datetime.date.today(), 'appointment_time': datetime.time(16, 30), 'status': 'Completed'}
        ]

        # 5. Consultations
        self.consultations = [
            {'id': 1, 'patient_id': 1, 'doctor_id': 2, 'doctor_name': 'Dr. Priya', 'consultation_date': '10-08-2026', 'symptoms': 'High fever, acute chills', 'diagnosis': 'Viral Fever', 'treatment_prescription': 'Paracetamol 500mg (1-1-1), Rest for 3 days', 'created_at': datetime.datetime.now()},
            {'id': 2, 'patient_id': 3, 'doctor_id': 2, 'doctor_name': 'Dr. Priya', 'consultation_date': '08-08-2026', 'symptoms': 'High BP readings, dizziness', 'diagnosis': 'Stage-1 Hypertension', 'treatment_prescription': 'Amlodipine 5mg (1-0-0), Low Salt Diet', 'created_at': datetime.datetime.now()},
            {'id': 3, 'patient_id': 5, 'doctor_id': 3, 'doctor_name': 'Dr. Rajesh', 'consultation_date': '05-08-2026', 'symptoms': 'Increased thirst, fatigue', 'diagnosis': 'Type-2 Diabetes Mellitus', 'treatment_prescription': 'Metformin 500mg (1-0-1), Exercise', 'created_at': datetime.datetime.now()},
            {'id': 4, 'patient_id': 10, 'doctor_id': 3, 'doctor_name': 'Dr. Rajesh', 'consultation_date': '02-08-2026', 'symptoms': 'Severe unilateral throbbing headache', 'diagnosis': 'Chronic Migraine', 'treatment_prescription': 'Sumatriptan 50mg as needed, Stress reduction', 'created_at': datetime.datetime.now()}
        ]

        # 6. Prescriptions
        self.prescriptions = [
            {'id': 1, 'patient_id': 1, 'doctor_name': 'Dr. Priya', 'medicine': 'Paracetamol 500mg', 'dosage': '1 Tablet', 'frequency': 'Thrice Daily', 'duration': '5 Days', 'start_date': '10-08-2026', 'created_at': datetime.datetime.now()},
            {'id': 2, 'patient_id': 3, 'doctor_name': 'Dr. Priya', 'medicine': 'Amlodipine 5mg', 'dosage': '1 Tablet', 'frequency': 'Once Daily (Morning)', 'duration': '30 Days', 'start_date': '08-08-2026', 'created_at': datetime.datetime.now()},
            {'id': 3, 'patient_id': 5, 'doctor_name': 'Dr. Rajesh', 'medicine': 'Metformin 500mg', 'dosage': '1 Tablet', 'frequency': 'Twice Daily (With Meals)', 'duration': '30 Days', 'start_date': '05-08-2026', 'created_at': datetime.datetime.now()},
            {'id': 4, 'patient_id': 10, 'doctor_name': 'Dr. Rajesh', 'medicine': 'Sumatriptan 50mg', 'dosage': '1 Tablet', 'frequency': 'As needed for pain', 'duration': '10 Days', 'start_date': '02-08-2026', 'created_at': datetime.datetime.now()}
        ]

        # 7. Lab Reports
        self.lab_reports = [
            {'id': 1, 'patient_id': 1, 'test_name': 'Complete Blood Count (CBC)', 'result': 'Normal', 'report_file': 'report_cbc_1001.pdf', 'test_date': '10-08-2026', 'created_at': datetime.datetime.now()},
            {'id': 2, 'patient_id': 2, 'test_name': 'Lipid Profile Test', 'result': 'Pending', 'report_file': 'report_lipid_1002.pdf', 'test_date': '10-08-2026', 'created_at': datetime.datetime.now()},
            {'id': 3, 'patient_id': 3, 'test_name': 'Kidney Function Test (KFT)', 'result': 'Normal', 'report_file': 'report_kft_1003.pdf', 'test_date': '08-08-2026', 'created_at': datetime.datetime.now()},
            {'id': 4, 'patient_id': 5, 'test_name': 'Fasting Blood Sugar & HbA1c', 'result': 'Critical', 'report_file': 'report_hba1c_1005.pdf', 'test_date': '05-08-2026', 'created_at': datetime.datetime.now()},
            {'id': 5, 'patient_id': 7, 'test_name': 'Lipid Profile Test', 'result': 'Borderline', 'report_file': 'report_lipid_1007.pdf', 'test_date': '03-08-2026', 'created_at': datetime.datetime.now()}
        ]

        # 8. EHR Allergies & Diagnoses
        self.allergies = [
            {'id': 1, 'patient_id': 1, 'allergen': 'Penicillin', 'reaction': 'Skin Rash and Itching', 'added_on': '10-08-2026'},
            {'id': 2, 'patient_id': 5, 'allergen': 'Sulfa Drugs', 'reaction': 'Hives & Breathing Difficulty', 'added_on': '05-08-2026'},
            {'id': 3, 'patient_id': 6, 'allergen': 'Dust Mites', 'reaction': 'Bronchospasm', 'added_on': '01-08-2026'}
        ]

        self.diagnoses = [
            {'id': 1, 'patient_id': 1, 'diagnosis_date': '10-08-2026', 'diagnosis_name': 'Viral Fever', 'doctor_name': 'Dr. Priya', 'notes': 'Responded well to antipyretics.'},
            {'id': 2, 'patient_id': 3, 'diagnosis_date': '08-08-2026', 'diagnosis_name': 'Hypertension', 'doctor_name': 'Dr. Priya', 'notes': 'BP measured 145/95 mmHg.'},
            {'id': 3, 'patient_id': 5, 'diagnosis_date': '05-08-2026', 'diagnosis_name': 'Type-2 Diabetes', 'doctor_name': 'Dr. Rajesh', 'notes': 'HbA1c level: 7.8%.'},
            {'id': 4, 'patient_id': 7, 'diagnosis_date': '03-08-2026', 'diagnosis_name': 'Hyperlipidemia', 'doctor_name': 'Dr. John Smith', 'notes': 'Elevated LDL cholesterol.'}
        ]

        # 9. Pharmacy Inventory & Dispensed
        self.medicines = [
            {'id': 1, 'medicine_code': 'MED1001', 'name': 'Paracetamol 500mg', 'manufacturer': 'Sun Pharma', 'category': 'Analgesics', 'batch_number': 'BAT-2026-01', 'mfg_date': datetime.date(2025, 1, 10), 'exp_date': datetime.date(2027, 12, 31), 'price': 3.50, 'stock': 450, 'min_stock_alert': 10},
            {'id': 2, 'medicine_code': 'MED1002', 'name': 'Amoxicillin 250mg', 'manufacturer': 'Cipla Ltd', 'category': 'Antibiotics', 'batch_number': 'BAT-2026-02', 'mfg_date': datetime.date(2025, 3, 15), 'exp_date': datetime.date(2026, 11, 20), 'price': 12.00, 'stock': 180, 'min_stock_alert': 10},
            {'id': 3, 'medicine_code': 'MED1003', 'name': 'Cetirizine 10mg', 'manufacturer': 'Dr. Reddys', 'category': 'Antihistamines', 'batch_number': 'BAT-2025-88', 'mfg_date': datetime.date(2024, 5, 1), 'exp_date': datetime.date(2026, 1, 1), 'price': 4.00, 'stock': 8, 'min_stock_alert': 10},
            {'id': 4, 'medicine_code': 'MED1004', 'name': 'Pantoprazole 40mg', 'manufacturer': 'Lupin Pharma', 'category': 'Antacids', 'batch_number': 'BAT-2026-04', 'mfg_date': datetime.date(2025, 2, 20), 'exp_date': datetime.date(2027, 6, 30), 'price': 8.50, 'stock': 250, 'min_stock_alert': 10},
            {'id': 5, 'medicine_code': 'MED1005', 'name': 'Metformin 500mg', 'manufacturer': 'Torrent Pharma', 'category': 'Antidiabetic', 'batch_number': 'BAT-2026-05', 'mfg_date': datetime.date(2025, 4, 5), 'exp_date': datetime.date(2028, 4, 5), 'price': 6.00, 'stock': 320, 'min_stock_alert': 10}
        ]

        self.dispensed_medicines = [
            {'id': 1, 'patient_id': 1, 'medicine_id': 1, 'pharmacist_name': 'Pharm Pharmacist', 'quantity': 10, 'unit_price': 3.50, 'total_price': 35.0, 'dispensed_at': datetime.datetime.now()}
        ]

        # 10. Billing Invoices
        self.bills = [
            {'id': 1, 'invoice_number': 'INV-2026-0001', 'patient_id': 1, 'consultation_charges': 500.0, 'laboratory_charges': 350.0, 'medicine_charges': 35.0, 'additional_charges': 0.0, 'room_charges': 0.0, 'subtotal': 885.0, 'gst_rate': 18.0, 'gst_amount': 159.30, 'total_amount': 1044.30, 'payment_method': 'UPI', 'payment_status': 'Paid', 'created_at': datetime.datetime.now(), 'paid_at': datetime.datetime.now()},
            {'id': 2, 'invoice_number': 'INV-2026-0002', 'patient_id': 2, 'consultation_charges': 500.0, 'laboratory_charges': 250.0, 'medicine_charges': 12.0, 'additional_charges': 0.0, 'room_charges': 0.0, 'subtotal': 762.0, 'gst_rate': 18.0, 'gst_amount': 137.16, 'total_amount': 899.16, 'payment_method': 'Cash', 'payment_status': 'Pending', 'created_at': datetime.datetime.now(), 'paid_at': None},
            {'id': 3, 'invoice_number': 'INV-2026-0003', 'patient_id': 5, 'consultation_charges': 700.0, 'laboratory_charges': 600.0, 'medicine_charges': 180.0, 'additional_charges': 0.0, 'room_charges': 0.0, 'subtotal': 1480.0, 'gst_rate': 18.0, 'gst_amount': 266.40, 'total_amount': 1746.40, 'payment_method': 'Card', 'payment_status': 'Paid', 'created_at': datetime.datetime.now(), 'paid_at': datetime.datetime.now()}
        ]

        # 11. Notifications & Support Tickets & Feedback
        self.notifications = [
            {'id': 1, 'title': 'Appointment Confirmed', 'message': 'Your appointment with Dr. Priya is scheduled for today at 10:30 AM.', 'date': datetime.datetime.now(), 'status': 'unread', 'recipient_role': 'Patient', 'recipient_user_id': None, 'notification_type': 'Appointment Reminder'},
            {'id': 2, 'title': 'Prescription Ready', 'message': 'Prescription for Paracetamol 500mg has been generated by Dr. Priya.', 'date': datetime.datetime.now(), 'status': 'unread', 'recipient_role': 'Patient', 'recipient_user_id': None, 'notification_type': 'Prescription Ready'},
            {'id': 3, 'title': 'Lab Report Completed', 'message': 'CBC Blood Test report for Rahul Kumar is ready for download.', 'date': datetime.datetime.now(), 'status': 'read', 'recipient_role': 'Doctor', 'recipient_user_id': None, 'notification_type': 'Lab Report Ready'}
        ]

        self.support_tickets = [
            {'id': 1, 'patient_name': 'Rahul Kumar', 'email': 'patient@gmail.com', 'subject': 'Insurance Claim Inquiry', 'message': 'Need assistance downloading detailed itemized medical bills.', 'status': 'Open', 'created_at': datetime.datetime.now()}
        ]

        self.patient_feedbacks = [
            {'id': 1, 'patient_id': 1, 'doctor_id': 2, 'rating': 5, 'comments': 'Dr. Priya was extremely attentive and explained the diagnosis clearly.', 'created_at': datetime.datetime.now()},
            {'id': 2, 'patient_id': 2, 'doctor_id': 1, 'rating': 4, 'comments': 'Prompt service and clean facility. Highly recommended!', 'created_at': datetime.datetime.now()}
        ]

        self.login_logs = []

    # ------------------ HELPER FUNCTIONS & DAOs ------------------

    def validate_aadhaar(self, aadhaar_str):
        if not aadhaar_str:
            raise ValueError("Aadhaar number is required and cannot be empty.")
        clean_val = str(aadhaar_str).replace(' ', '').replace('-', '').strip()
        if not clean_val or not clean_val.isdigit() or len(clean_val) != 12:
            raise ValueError("Aadhaar number must be exactly 12 numeric digits.")
        return clean_val

    def mask_aadhaar(self, aadhaar_str):
        if not aadhaar_str:
            return "N/A"
        clean_val = str(aadhaar_str).replace(' ', '').replace('-', '').strip()
        if len(clean_val) != 12:
            return "N/A"
        return f"XXXX-XXXX-{clean_val[-4:]}"

    def get_user_by_id(self, user_id):
        for u in self.users:
            if u.id == user_id:
                return u
        return None

    def get_user_by_email(self, email):
        for u in self.users:
            if u.email.lower() == email.lower():
                return u
        return None

    def get_patient_raw_by_id(self, patient_id):
        for p in self.patients:
            if p['id'] == patient_id:
                p_copy = dict(p)
                p_copy['masked_aadhaar'] = self.mask_aadhaar(p_copy.get('aadhaar_number'))
                return p_copy
        return None

    def get_patient_by_id(self, patient_id):
        p_raw = self.get_patient_raw_by_id(patient_id)
        if not p_raw:
            return None
        p_copy = dict(p_raw)
        p_copy['consultations'] = [dict(c) for c in self.consultations if c['patient_id'] == patient_id]
        p_copy['prescriptions'] = [dict(pr) for pr in self.prescriptions if pr['patient_id'] == patient_id]
        p_copy['lab_reports'] = [dict(l) for l in self.lab_reports if l['patient_id'] == patient_id]
        p_copy['allergies'] = [dict(a) for a in self.allergies if a['patient_id'] == patient_id]
        p_copy['diagnoses'] = [dict(d) for d in self.diagnoses if d['patient_id'] == patient_id]
        p_copy['dispensed_medicines'] = [dict(dm) for dm in self.dispensed_medicines if dm['patient_id'] == patient_id]
        p_copy['bills'] = [dict(b) for b in self.bills if b['patient_id'] == patient_id]
        p_copy['feedbacks'] = [dict(f) for f in self.patient_feedbacks if f['patient_id'] == patient_id]
        return p_copy

    def get_patient_by_code(self, code):
        for p in self.patients:
            if p['patient_code'].lower() == code.lower():
                return self.get_patient_by_id(p['id'])
        return None

    def get_patient_by_aadhaar(self, aadhaar_str):
        clean_aadhaar = str(aadhaar_str).replace(' ', '').replace('-', '').strip()
        for p in self.patients:
            if p.get('aadhaar_number') == clean_aadhaar:
                return self.get_patient_by_id(p['id'])
        return None

    def search_patients(self, query_str):
        if not query_str:
            return []
        q = query_str.lower().strip()
        clean_q = q.replace(' ', '').replace('-', '')
        results = []
        for p in self.patients:
            p_code = p['patient_code'].lower()
            p_name = p['full_name'].lower()
            p_phone = p['phone_number'].lower()
            p_email = p['email'].lower()
            p_aadhaar = (p.get('aadhaar_number') or '').lower()

            if (q in p_code or q in p_name or q in p_phone or q in p_email or
                clean_q == p_aadhaar or clean_q in p_aadhaar):
                results.append(self.get_patient_by_id(p['id']))
        return results

    def add_patient(self, data):
        aadhaar_clean = self.validate_aadhaar(data.get('aadhaar_number'))

        # Check unique Aadhaar
        if self.get_patient_by_aadhaar(aadhaar_clean):
            raise ValueError("Patient with this Aadhaar number already exists.")

        new_id = max([p['id'] for p in self.patients], default=0) + 1
        new_code = f"PAT{new_id + 1000}"

        p = {
            'id': new_id,
            'patient_code': new_code,
            'full_name': data.get('full_name'),
            'age': int(data.get('age', 30)),
            'gender': data.get('gender', 'Male'),
            'phone_number': data.get('phone_number'),
            'email': data.get('email', f"patient{new_id}@example.com"),
            'address': data.get('address', 'N/A'),
            'blood_group': data.get('blood_group', 'O+'),
            'aadhaar_number': aadhaar_clean,
            'date_of_birth': data.get('date_of_birth', '01-01-1995'),
            'height': '170 cm',
            'weight': '70 kg',
            'bmi': '24.2',
            'smoking': 'No',
            'alcohol': 'No',
            'chronic_diseases': 'No',
            'remarks': 'Newly registered patient.',
            'medical_history': data.get('medical_history', 'None')
        }
        self.patients.append(p)

        # Also create User record for login
        new_u_id = max([u.id for u in self.users], default=0) + 1
        u = User(new_u_id, p['full_name'], p['email'], p['phone_number'], 'Patient', generate_password_hash('patient123'))
        self.users.append(u)

        return self.get_patient_by_id(new_id)

    def get_doctor_by_id(self, doctor_id):
        for d in self.doctors:
            if d['id'] == doctor_id:
                return dict(d)
        return None

    def get_all_patients(self):
        return [self.get_patient_by_id(p['id']) for p in self.patients]

    def get_all_doctors(self):
        return [dict(d) for d in self.doctors]

    # ------------------ APPOINTMENTS ------------------
    def get_all_appointments(self):
        result = []
        for app_rec in self.appointments:
            a = dict(app_rec)
            a['patient'] = self.get_patient_raw_by_id(a['patient_id'])
            a['doctor'] = self.get_doctor_by_id(a['doctor_id'])
            result.append(a)
        return result

    def get_appointments_by_patient(self, patient_id):
        return [a for a in self.get_all_appointments() if a['patient_id'] == patient_id]

    def get_appointments_by_doctor(self, doctor_id):
        return [a for a in self.get_all_appointments() if a['doctor_id'] == doctor_id]

    def add_appointment(self, patient_id, doctor_id, app_date, app_time):
        new_id = max([a['id'] for a in self.appointments], default=0) + 1
        a = {
            'id': new_id,
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            'appointment_date': app_date,
            'appointment_time': app_time,
            'status': 'Scheduled'
        }
        self.appointments.append(a)
        return a

    # ------------------ CONSULTATIONS & AUTOMATED WORKFLOW ------------------
    def get_all_consultations(self):
        result = []
        for c in self.consultations:
            c_copy = dict(c)
            c_copy['patient'] = self.get_patient_raw_by_id(c['patient_id'])
            result.append(c_copy)
        return result

    def get_consultations_by_patient(self, patient_id):
        return [c for c in self.get_all_consultations() if c['patient_id'] == patient_id]

    def add_consultation(self, data):
        patient_id = data.get('patient_id')
        if not patient_id and data.get('patient_name'):
            p = next((p for p in self.patients if p['full_name'].lower() == data.get('patient_name').lower()), None)
            patient_id = p['id'] if p else 1
        patient_id = int(patient_id or 1)

        doctor_name = data.get('doctor_name', 'Dr. Priya')
        doc = next((d for d in self.doctors if d['doctor_name'].lower() in doctor_name.lower()), self.doctors[0])
        consult_date = data.get('consultation_date', datetime.datetime.now().strftime('%d-%m-%Y'))
        symptoms = data.get('symptoms', 'N/A')
        diagnosis = data.get('diagnosis', 'Observation')
        treatment = data.get('treatment_prescription', 'Rest')

        new_id = max([c['id'] for c in self.consultations], default=0) + 1
        c = {
            'id': new_id,
            'patient_id': patient_id,
            'doctor_id': doc['id'],
            'doctor_name': doctor_name,
            'consultation_date': consult_date,
            'symptoms': symptoms,
            'diagnosis': diagnosis,
            'treatment_prescription': treatment,
            'created_at': datetime.datetime.now()
        }
        self.consultations.append(c)

        # Automated Workflow
        # 1. Update appointment to Completed
        for app_rec in self.appointments:
            if app_rec['patient_id'] == patient_id and app_rec['status'] == 'Scheduled':
                app_rec['status'] = 'Completed'

        # 2. Add Diagnosis to EHR
        diag_id = max([d['id'] for d in self.diagnoses], default=0) + 1
        self.diagnoses.append({
            'id': diag_id,
            'patient_id': patient_id,
            'diagnosis_date': consult_date,
            'diagnosis_name': diagnosis,
            'doctor_name': doctor_name,
            'notes': symptoms
        })

        # 3. Auto-generate Prescription if medicine mentioned
        self.add_prescription({
            'patient_id': patient_id,
            'doctor_name': doctor_name,
            'medicine': treatment.split(',')[0] if ',' in treatment else treatment,
            'dosage': '1 Tablet',
            'frequency': 'Twice Daily',
            'duration': '5 Days',
            'start_date': consult_date
        })

        # 4. Auto-generate Notification to Patient
        self.add_notification('Consultation Completed', f'Consultation completed with {doctor_name}. Diagnosis: {diagnosis}', 'Prescription Ready', 'Patient')
        # Notify Doctor role about the new consultation record
        self.add_notification('New Consultation Record', f'Consultation saved for patient ID {patient_id}. Diagnosis: {diagnosis}.', 'Lab Report Ready', 'Doctor')

        return c

    # ------------------ PRESCRIPTIONS ------------------
    def get_all_prescriptions(self):
        result = []
        for pr in self.prescriptions:
            pr_copy = dict(pr)
            pr_copy['patient'] = self.get_patient_raw_by_id(pr['patient_id'])
            result.append(pr_copy)
        return result

    def get_prescriptions_by_patient(self, patient_id):
        return [pr for pr in self.get_all_prescriptions() if pr['patient_id'] == patient_id]

    def add_prescription(self, data):
        patient_id = int(data.get('patient_id'))
        new_id = max([pr['id'] for pr in self.prescriptions], default=0) + 1
        pr = {
            'id': new_id,
            'patient_id': patient_id,
            'doctor_name': data.get('doctor_name', 'Dr. Priya'),
            'medicine': data.get('medicine', 'Paracetamol 500mg'),
            'dosage': data.get('dosage', '1 Tablet'),
            'frequency': data.get('frequency', 'Twice Daily'),
            'duration': data.get('duration', '5 Days'),
            'start_date': data.get('start_date', datetime.datetime.now().strftime('%d-%m-%Y')),
            'created_at': datetime.datetime.now()
        }
        self.prescriptions.append(pr)
        # Auto-notify Patient that prescription is ready
        patient = self.get_patient_raw_by_id(patient_id)
        if patient:
            self.add_notification(
                'Prescription Ready',
                f'New prescription for {pr["medicine"]} ({pr["dosage"]}) by {pr["doctor_name"]} is ready.',
                'Prescription Ready', 'Patient'
            )
        return pr

    # ------------------ LAB REPORTS ------------------
    def get_all_lab_reports(self):
        result = []
        for l in self.lab_reports:
            l_copy = dict(l)
            l_copy['patient'] = self.get_patient_raw_by_id(l['patient_id'])
            result.append(l_copy)
        return result

    def get_lab_reports_by_patient(self, patient_id):
        return [l for l in self.get_all_lab_reports() if l['patient_id'] == patient_id]

    def add_lab_report(self, data):
        patient_id = int(data.get('patient_id'))
        patient = self.get_patient_raw_by_id(patient_id)
        new_id = max([l['id'] for l in self.lab_reports], default=0) + 1
        l = {
            'id': new_id,
            'patient_id': patient_id,
            'test_name': data.get('test_name', 'Complete Blood Count (CBC)'),
            'test_date': data.get('test_date', datetime.datetime.now().strftime('%d-%m-%Y')),
            'result': data.get('result', 'Pending'),
            'report_file': f"report_{(patient['patient_code'] if patient else 'pat').lower()}_{new_id}.pdf",
            'created_at': datetime.datetime.now()
        }
        self.lab_reports.append(l)

        if patient:
            self.add_notification('Lab Test Requested', f'Lab test "{l["test_name"]}" requested for {patient["full_name"]}.', 'Lab Report Ready', 'Laboratory Staff')
        return l

    def add_allergy(self, data):
        """Add allergy directly (called from EHR modal or API)."""
        patient_id = int(data.get('patient_id', 0))
        patient = self.get_patient_raw_by_id(patient_id)
        new_id = max([a['id'] for a in self.allergies], default=0) + 1
        today_str = datetime.datetime.now().strftime('%d-%m-%Y')
        a = {
            'id': new_id,
            'patient_id': patient_id,
            'allergen': data.get('allergen', 'Unknown'),
            'reaction': data.get('reaction', 'Unknown'),
            'added_on': today_str
        }
        self.allergies.append(a)
        if patient:
            self.add_notification(
                'Allergy Recorded',
                f'New allergy "{a["allergen"]}" recorded for {patient["full_name"]}. Reaction: {a["reaction"]}.',
                'Hospital Announcement', 'Doctor'
            )
            self.add_notification(
                'Allergy Alert Added',
                f'A new allergy alert has been added to your health record: {a["allergen"]}.',
                'Hospital Announcement', 'Patient'
            )
        return a

    def add_diagnosis_direct(self, data):
        """Add diagnosis directly (called from EHR modal or API)."""
        patient_id = int(data.get('patient_id', 0))
        patient = self.get_patient_raw_by_id(patient_id)
        new_id = max([d['id'] for d in self.diagnoses], default=0) + 1
        today_str = datetime.datetime.now().strftime('%d-%m-%Y')
        d = {
            'id': new_id,
            'patient_id': patient_id,
            'diagnosis_date': data.get('diagnosis_date', today_str),
            'diagnosis_name': data.get('diagnosis_name', 'Unspecified'),
            'doctor_name': data.get('doctor_name', 'Dr. Priya'),
            'notes': data.get('notes', '')
        }
        self.diagnoses.append(d)
        if patient:
            self.add_notification(
                'New Diagnosis Added',
                f'Diagnosis "{d["diagnosis_name"]}" recorded for {patient["full_name"]} by {d["doctor_name"]}.',
                'Hospital Announcement', 'Patient'
            )
        return d

    def update_lab_result(self, report_id, result, report_file=None):
        for l in self.lab_reports:
            if l['id'] == report_id:
                l['result'] = result
                if report_file:
                    l['report_file'] = report_file
                self.add_notification('Lab Report Status Updated', f'Lab report for "{l["test_name"]}" updated to {result}.', 'Lab Report Ready', 'Patient')
                return l
        return None

    # ------------------ EHR SUMMARY & VITALS ------------------
    def get_ehr_summary(self, patient_id):
        return self.get_patient_by_id(patient_id)

    def update_ehr_vitals(self, patient_id, data):
        for p in self.patients:
            if p['id'] == patient_id:
                p['height'] = data.get('height', p['height'])
                p['weight'] = data.get('weight', p['weight'])
                p['bmi'] = data.get('bmi', p['bmi'])
                p['smoking'] = data.get('smoking', p['smoking'])
                p['alcohol'] = data.get('alcohol', p['alcohol'])
                p['chronic_diseases'] = data.get('chronic_diseases', p['chronic_diseases'])
                p['remarks'] = data.get('remarks', p['remarks'])
                return self.get_patient_by_id(patient_id)
        return None

    # ------------------ PHARMACY & BILLING ------------------
    def get_all_medicines(self):
        return [dict(m) for m in self.medicines]

    def add_medicine(self, data):
        new_id = max([m['id'] for m in self.medicines], default=0) + 1
        m = {
            'id': new_id,
            'medicine_code': f"MED{new_id + 1000}",
            'name': data.get('name'),
            'manufacturer': data.get('manufacturer'),
            'category': data.get('category'),
            'batch_number': data.get('batch_number'),
            'mfg_date': data.get('mfg_date'),
            'exp_date': data.get('exp_date'),
            'price': float(data.get('price', 0.0)),
            'stock': int(data.get('stock', 0)),
            'min_stock_alert': 10
        }
        self.medicines.append(m)
        return m

    def dispense_medicine(self, patient_id, medicine_id, quantity, pharmacist_name='System Pharmacist'):
        med = next((m for m in self.medicines if m['id'] == medicine_id), None)
        if not med or med['stock'] < quantity:
            raise ValueError("Insufficient stock or medicine not found.")

        med['stock'] -= quantity
        total_price = med['price'] * quantity
        new_id = max([dm['id'] for dm in self.dispensed_medicines], default=0) + 1
        disp = {
            'id': new_id,
            'patient_id': patient_id,
            'medicine_id': medicine_id,
            'pharmacist_name': pharmacist_name,
            'quantity': quantity,
            'unit_price': med['price'],
            'total_price': total_price,
            'dispensed_at': datetime.datetime.now()
        }
        self.dispensed_medicines.append(disp)
        self.add_notification('Medicine Dispensed', f'{quantity} unit(s) of {med["name"]} dispensed. Total: ₹{total_price:.2f}', 'Prescription Ready', 'Patient')
        return disp

    def get_all_bills(self):
        result = []
        for b in self.bills:
            b_copy = dict(b)
            b_copy['patient'] = self.get_patient_raw_by_id(b['patient_id'])
            result.append(b_copy)
        return result

    def get_bill_by_id(self, bill_id):
        for b in self.get_all_bills():
            if b['id'] == bill_id:
                return b
        return None

    def create_bill(self, patient_id, consultation_charges, laboratory_charges, medicine_charges, additional_charges=0.0, room_charges=0.0, payment_method='Cash', payment_status='Pending'):
        patient = self.get_patient_raw_by_id(patient_id)
        subtotal = consultation_charges + laboratory_charges + medicine_charges + additional_charges + room_charges
        gst_rate = 18.0
        gst_amount = subtotal * (gst_rate / 100.0)
        total_amount = subtotal + gst_amount

        new_id = max([b['id'] for b in self.bills], default=0) + 1
        inv_code = f"INV-2026-{new_id + 1000:04d}"

        b = {
            'id': new_id,
            'invoice_number': inv_code,
            'patient_id': patient_id,
            'consultation_charges': consultation_charges,
            'laboratory_charges': laboratory_charges,
            'medicine_charges': medicine_charges,
            'additional_charges': additional_charges,
            'room_charges': room_charges,
            'subtotal': subtotal,
            'gst_rate': gst_rate,
            'gst_amount': gst_amount,
            'total_amount': total_amount,
            'payment_method': payment_method,
            'payment_status': payment_status,
            'created_at': datetime.datetime.now(),
            'paid_at': datetime.datetime.now() if payment_status == 'Paid' else None
        }
        self.bills.append(b)
        if patient:
            self.add_notification('New Bill Generated', f'Invoice {inv_code} created for {patient["full_name"]}. Total: ₹{total_amount:.2f}', 'Billing Reminder', 'Patient')
        return b

    # ------------------ NOTIFICATIONS & FEEDBACK ------------------
    def get_notifications(self, role='all', user_id=None):
        results = []
        for n in self.notifications:
            if n['recipient_role'] == 'all' or n['recipient_role'] == role or (user_id and n.get('recipient_user_id') == user_id):
                results.append(dict(n))
        return sorted(results, key=lambda x: x['id'], reverse=True)

    def mark_notification_read(self, notif_id):
        for n in self.notifications:
            if n['id'] == notif_id:
                n['status'] = 'read'
                return dict(n)
        return None

    def mark_notification_unread(self, notif_id):
        for n in self.notifications:
            if n['id'] == notif_id:
                n['status'] = 'unread'
                return dict(n)
        return None

    def mark_notification_delivered(self, notif_id):
        for n in self.notifications:
            if n['id'] == notif_id:
                n['status'] = 'delivered'
                return dict(n)
        return None

    def add_notification(self, title, message, notification_type, recipient_role='all', recipient_user_id=None):
        new_id = max([n['id'] for n in self.notifications], default=0) + 1
        n = {
            'id': new_id,
            'title': title,
            'message': message,
            'date': datetime.datetime.now(),
            'status': 'unread',
            'recipient_role': recipient_role,
            'recipient_user_id': recipient_user_id,
            'notification_type': notification_type
        }
        self.notifications.append(n)
        return n

    def add_patient_feedback(self, patient_id, doctor_id, rating, comments):
        new_id = max([f['id'] for f in self.patient_feedbacks], default=0) + 1
        fb = {
            'id': new_id,
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            'rating': rating,
            'comments': comments,
            'created_at': datetime.datetime.now()
        }
        self.patient_feedbacks.append(fb)
        return fb

# Single Global Application DataStore Instance
data_store = DataStore()
