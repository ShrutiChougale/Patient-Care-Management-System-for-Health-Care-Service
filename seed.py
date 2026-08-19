from app import app, db
from models.models import User, Patient, Doctor, Appointment, Consultation, Prescription, LabReport, Allergy, Diagnosis, Medicine, DispensedMedicine, Bill, Notification, LoginLog, SupportTicket, PatientFeedback
import datetime

def seed_database():
    with app.app_context():
        # Ensure database tables exist with updated schema
        db.drop_all()
        db.create_all()

        # 1. Seed System Users (6 Roles)
        users_data = [
            {'full_name': 'System Admin', 'email': 'admin@gmail.com', 'phone_number': '1234567890', 'role': 'Admin', 'pass': 'admin123'},
            {'full_name': 'Dr. John Smith', 'email': 'doctor@gmail.com', 'phone_number': '1234567891', 'role': 'Doctor', 'pass': 'doctor123'},
            {'full_name': 'Dr. Priya', 'email': 'drpriya@gmail.com', 'phone_number': '9988776654', 'role': 'Doctor', 'pass': 'doctor123'},
            {'full_name': 'Nurse Test', 'email': 'nurse@gmail.com', 'phone_number': '1234567892', 'role': 'Nurse', 'pass': 'nurse123'},
            {'full_name': 'Pharm Pharmacist', 'email': 'pharmacist@gmail.com', 'phone_number': '1234567893', 'role': 'Pharmacist', 'pass': 'pharmacist123'},
            {'full_name': 'Lab Technician', 'email': 'lab@gmail.com', 'phone_number': '1234567894', 'role': 'Laboratory Staff', 'pass': 'lab123'},
            {'full_name': 'Rahul Kumar', 'email': 'patient@gmail.com', 'phone_number': '9876543210', 'role': 'Patient', 'pass': 'patient123'}
        ]

        for udata in users_data:
            existing = User.query.filter_by(email=udata['email']).first()
            if not existing:
                u = User(full_name=udata['full_name'], email=udata['email'], phone_number=udata['phone_number'], role=udata['role'])
                u.set_password(udata['pass'])
                db.session.add(u)
        db.session.commit()

        # 2. Seed Doctors
        doctors_data = [
            {'name': 'Dr. John Smith', 'spec': 'Cardiologist', 'qual': 'MD Cardiology', 'dept': 'Cardiology', 'phone': '9988776655', 'email': 'drjohn@example.com', 'time': '09:00 AM - 05:00 PM'},
            {'name': 'Dr. Priya', 'spec': 'Physician', 'qual': 'MBBS, MD', 'dept': 'General Medicine', 'phone': '9988776654', 'email': 'drpriya@example.com', 'time': '10:00 AM - 04:00 PM'},
            {'name': 'Dr. Rajesh', 'spec': 'Neurologist', 'qual': 'DM Neurology', 'dept': 'Neurology', 'phone': '9988776653', 'email': 'drrajesh@example.com', 'time': '11:00 AM - 06:00 PM'}
        ]
        for ddata in doctors_data:
            if not Doctor.query.filter_by(email_address=ddata['email']).first():
                d = Doctor(
                    doctor_name=ddata['name'],
                    specialization=ddata['spec'],
                    qualification=ddata['qual'],
                    department=ddata['dept'],
                    phone_number=ddata['phone'],
                    email_address=ddata['email'],
                    available_time=ddata['time']
                )
                db.session.add(d)
        db.session.commit()

        # 3. Seed 10 Distinct Patient Records (Each with mandatory, unique 12-digit Aadhaar Number)
        patients_data = [
            {
                'code': 'PAT1001', 'name': 'Rahul Kumar', 'age': 28, 'gender': 'Male', 'phone': '9876543210',
                'email': 'patient@gmail.com', 'address': '123 Green Street, Chennai', 'blood': 'O+', 'dob': '15-05-1996',
                'aadhaar': '100000000001', 'height': '175 cm', 'weight': '72 kg', 'bmi': '23.5', 'smoking': 'No', 'alcohol': 'Occasional',
                'chronic': 'No', 'remarks': 'Patient is healthy.'
            },
            {
                'code': 'PAT1002', 'name': 'Sneha Reddy', 'age': 26, 'gender': 'Female', 'phone': '9876543211',
                'email': 'sneha@example.com', 'address': '45 Park Avenue, Chennai', 'blood': 'A+', 'dob': '10-08-1998',
                'aadhaar': '100000000002', 'height': '162 cm', 'weight': '58 kg', 'bmi': '22.1', 'smoking': 'No', 'alcohol': 'No',
                'chronic': 'No', 'remarks': 'Good general health.'
            },
            {
                'code': 'PAT1003', 'name': 'Amit Verma', 'age': 35, 'gender': 'Male', 'phone': '9876543212',
                'email': 'amit@example.com', 'address': '88 Lake Road, Chennai', 'blood': 'B+', 'dob': '12-03-1989',
                'aadhaar': '100000000003', 'height': '178 cm', 'weight': '78 kg', 'bmi': '24.6', 'smoking': 'No', 'alcohol': 'Social',
                'chronic': 'Hypertension', 'remarks': 'Requires regular checkup.'
            },
            {
                'code': 'PAT1004', 'name': 'Pooja Sharma', 'age': 31, 'gender': 'Female', 'phone': '9876543213',
                'email': 'pooja@example.com', 'address': '12 MG Road, Chennai', 'blood': 'AB+', 'dob': '05-11-1993',
                'aadhaar': '100000000004', 'height': '165 cm', 'weight': '60 kg', 'bmi': '22.0', 'smoking': 'No', 'alcohol': 'No',
                'chronic': 'No', 'remarks': 'Under observation for gastritis.'
            },
            {
                'code': 'PAT1005', 'name': 'Vikram Malhotra', 'age': 42, 'gender': 'Male', 'phone': '9876543214',
                'email': 'vikram@example.com', 'address': '102 Civil Lines, Delhi', 'blood': 'O-', 'dob': '20-01-1984',
                'aadhaar': '100000000005', 'height': '180 cm', 'weight': '85 kg', 'bmi': '26.2', 'smoking': 'Yes', 'alcohol': 'Regular',
                'chronic': 'Type-2 Diabetes', 'remarks': 'Insulin dosage under evaluation.'
            },
            {
                'code': 'PAT1006', 'name': 'Ananya Roy', 'age': 24, 'gender': 'Female', 'phone': '9876543215',
                'email': 'ananya@example.com', 'address': '77 Salt Lake, Kolkata', 'blood': 'A-', 'dob': '14-07-2000',
                'aadhaar': '100000000006', 'height': '158 cm', 'weight': '52 kg', 'bmi': '20.8', 'smoking': 'No', 'alcohol': 'No',
                'chronic': 'Asthma', 'remarks': 'Prescribed Inhaler.'
            },
            {
                'code': 'PAT1007', 'name': 'Suresh Nair', 'age': 50, 'gender': 'Male', 'phone': '9876543216',
                'email': 'suresh@example.com', 'address': '19 Marine Drive, Mumbai', 'blood': 'B-', 'dob': '30-09-1974',
                'aadhaar': '100000000007', 'height': '170 cm', 'weight': '75 kg', 'bmi': '25.9', 'smoking': 'No', 'alcohol': 'Social',
                'chronic': 'High Cholesterol', 'remarks': 'Routine lipid monitoring.'
            },
            {
                'code': 'PAT1008', 'name': 'Meera Kapoor', 'age': 29, 'gender': 'Female', 'phone': '9876543217',
                'email': 'meera@example.com', 'address': '55 Jubilee Hills, Hyderabad', 'blood': 'AB-', 'dob': '18-02-1995',
                'aadhaar': '100000000008', 'height': '168 cm', 'weight': '64 kg', 'bmi': '22.7', 'smoking': 'No', 'alcohol': 'No',
                'chronic': 'Thyroid Deficiency', 'remarks': 'Thyroxine 50mcg daily.'
            },
            {
                'code': 'PAT1009', 'name': 'Rajesh Patel', 'age': 38, 'gender': 'Male', 'phone': '9876543218',
                'email': 'rajesh@example.com', 'address': '14 SG Highway, Ahmedabad', 'blood': 'O+', 'dob': '09-04-1986',
                'aadhaar': '100000000009', 'height': '172 cm', 'weight': '70 kg', 'bmi': '23.7', 'smoking': 'No', 'alcohol': 'No',
                'chronic': 'No', 'remarks': 'Annual executive health checkup.'
            },
            {
                'code': 'PAT1010', 'name': 'Deepa Iyer', 'age': 33, 'gender': 'Female', 'phone': '9876543219',
                'email': 'deepa@example.com', 'address': '90 Indiranagar, Bengaluru', 'blood': 'A+', 'dob': '25-12-1991',
                'aadhaar': '100000000010', 'height': '160 cm', 'weight': '56 kg', 'bmi': '21.9', 'smoking': 'No', 'alcohol': 'Occasional',
                'chronic': 'Migraine', 'remarks': 'Pain management consultation.'
            }
        ]

        for pdata in patients_data:
            p = Patient.query.filter_by(patient_code=pdata['code']).first()
            if not p:
                p = Patient(
                    patient_code=pdata['code'],
                    full_name=pdata['name'],
                    age=pdata['age'],
                    gender=pdata['gender'],
                    phone_number=pdata['phone'],
                    email=pdata['email'],
                    address=pdata['address'],
                    blood_group=pdata['blood'],
                    aadhaar_number=pdata['aadhaar'],
                    date_of_birth=pdata['dob'],
                    height=pdata['height'],
                    weight=pdata['weight'],
                    bmi=pdata['bmi'],
                    smoking=pdata['smoking'],
                    alcohol=pdata['alcohol'],
                    chronic_diseases=pdata['chronic'],
                    remarks=pdata['remarks']
                )
                db.session.add(p)
        db.session.commit()

        # Fetch references for relational linking via patient_id
        all_pats = {p.patient_code: p for p in Patient.query.all()}
        dr_priya = Doctor.query.filter_by(doctor_name='Dr. Priya').first() or Doctor.query.first()
        dr_john = Doctor.query.filter_by(doctor_name='Dr. John Smith').first() or Doctor.query.first()
        dr_rajesh = Doctor.query.filter_by(doctor_name='Dr. Rajesh').first() or Doctor.query.first()

        # 4. Seed Appointments across patients
        if not Appointment.query.first():
            appointments = [
                Appointment(patient_id=all_pats['PAT1001'].id, doctor_id=dr_priya.id, appointment_date=datetime.date.today(), appointment_time=datetime.time(10, 30), status='Completed'),
                Appointment(patient_id=all_pats['PAT1002'].id, doctor_id=dr_john.id, appointment_date=datetime.date.today(), appointment_time=datetime.time(11, 00), status='Scheduled'),
                Appointment(patient_id=all_pats['PAT1003'].id, doctor_id=dr_priya.id, appointment_date=datetime.date.today(), appointment_time=datetime.time(11, 30), status='Completed'),
                Appointment(patient_id=all_pats['PAT1005'].id, doctor_id=dr_rajesh.id, appointment_date=datetime.date.today(), appointment_time=datetime.time(14, 00), status='Completed'),
                Appointment(patient_id=all_pats['PAT1007'].id, doctor_id=dr_john.id, appointment_date=datetime.date.today(), appointment_time=datetime.time(15, 30), status='Scheduled'),
                Appointment(patient_id=all_pats['PAT1010'].id, doctor_id=dr_rajesh.id, appointment_date=datetime.date.today(), appointment_time=datetime.time(16, 30), status='Completed')
            ]
            db.session.add_all(appointments)
            db.session.commit()

        # 5. Seed Consultations across patients
        if not Consultation.query.first():
            consultations = [
                Consultation(patient_id=all_pats['PAT1001'].id, doctor_id=dr_priya.id, doctor_name=dr_priya.doctor_name, consultation_date='10-08-2026', symptoms='High fever, acute chills', diagnosis='Viral Fever', treatment_prescription='Paracetamol 500mg (1-1-1), Rest for 3 days'),
                Consultation(patient_id=all_pats['PAT1003'].id, doctor_id=dr_priya.id, doctor_name=dr_priya.doctor_name, consultation_date='08-08-2026', symptoms='High BP readings, dizziness', diagnosis='Stage-1 Hypertension', treatment_prescription='Amlodipine 5mg (1-0-0), Low Salt Diet'),
                Consultation(patient_id=all_pats['PAT1005'].id, doctor_id=dr_rajesh.id, doctor_name=dr_rajesh.doctor_name, consultation_date='05-08-2026', symptoms='Increased thirst, fatigue', diagnosis='Type-2 Diabetes Mellitus', treatment_prescription='Metformin 500mg (1-0-1), Exercise'),
                Consultation(patient_id=all_pats['PAT1010'].id, doctor_id=dr_rajesh.id, doctor_name=dr_rajesh.doctor_name, consultation_date='02-08-2026', symptoms='Severe unilateral throbbing headache', diagnosis='Chronic Migraine', treatment_prescription='Sumatriptan 50mg as needed, Stress reduction')
            ]
            db.session.add_all(consultations)
            db.session.commit()

        # 6. Seed EHR Diagnoses & Allergies
        if not Allergy.query.first():
            allergies = [
                Allergy(patient_id=all_pats['PAT1001'].id, allergen='Penicillin', reaction='Skin Rash and Itching', added_on='10-08-2026'),
                Allergy(patient_id=all_pats['PAT1005'].id, allergen='Sulfa Drugs', reaction='Hives & Breathing Difficulty', added_on='05-08-2026'),
                Allergy(patient_id=all_pats['PAT1006'].id, allergen='Dust Mites', reaction='Bronchospasm', added_on='01-08-2026')
            ]
            diagnoses = [
                Diagnosis(patient_id=all_pats['PAT1001'].id, diagnosis_date='10-08-2026', diagnosis_name='Viral Fever', doctor_name='Dr. Priya', notes='Responded well to antipyretics.'),
                Diagnosis(patient_id=all_pats['PAT1003'].id, diagnosis_date='08-08-2026', diagnosis_name='Hypertension', doctor_name='Dr. Priya', notes='BP measured 145/95 mmHg.'),
                Diagnosis(patient_id=all_pats['PAT1005'].id, diagnosis_date='05-08-2026', diagnosis_name='Type-2 Diabetes', doctor_name='Dr. Rajesh', notes='HbA1c level: 7.8%.'),
                Diagnosis(patient_id=all_pats['PAT1007'].id, diagnosis_date='03-08-2026', diagnosis_name='Hyperlipidemia', doctor_name='Dr. John Smith', notes='Elevated LDL cholesterol.')
            ]
            db.session.add_all(allergies + diagnoses)
            db.session.commit()

        # 7. Seed Medicines
        medicines_data = [
            {'code': 'MED1001', 'name': 'Paracetamol 500mg', 'mfg': 'Sun Pharma', 'cat': 'Analgesics', 'batch': 'BAT-2026-01', 'mfg_d': datetime.date(2025, 1, 10), 'exp_d': datetime.date(2027, 12, 31), 'price': 3.50, 'stock': 450},
            {'code': 'MED1002', 'name': 'Amoxicillin 250mg', 'mfg': 'Cipla Ltd', 'cat': 'Antibiotics', 'batch': 'BAT-2026-02', 'mfg_d': datetime.date(2025, 3, 15), 'exp_d': datetime.date(2026, 11, 20), 'price': 12.00, 'stock': 180},
            {'code': 'MED1003', 'name': 'Cetirizine 10mg', 'mfg': 'Dr. Reddys', 'cat': 'Antihistamines', 'batch': 'BAT-2025-88', 'mfg_d': datetime.date(2024, 5, 1), 'exp_d': datetime.date(2026, 1, 1), 'price': 4.00, 'stock': 8},
            {'code': 'MED1004', 'name': 'Pantoprazole 40mg', 'mfg': 'Lupin Pharma', 'cat': 'Antacids', 'batch': 'BAT-2026-04', 'mfg_d': datetime.date(2025, 2, 20), 'exp_d': datetime.date(2027, 6, 30), 'price': 8.50, 'stock': 250},
            {'code': 'MED1005', 'name': 'Metformin 500mg', 'mfg': 'Torrent Pharma', 'cat': 'Antidiabetic', 'batch': 'BAT-2026-05', 'mfg_d': datetime.date(2025, 4, 5), 'exp_d': datetime.date(2028, 4, 5), 'price': 6.00, 'stock': 320}
        ]
        for mdata in medicines_data:
            if not Medicine.query.filter_by(medicine_code=mdata['code']).first():
                m = Medicine(
                    medicine_code=mdata['code'], name=mdata['name'], manufacturer=mdata['mfg'],
                    category=mdata['cat'], batch_number=mdata['batch'], mfg_date=mdata['mfg_d'],
                    exp_date=mdata['exp_d'], price=mdata['price'], stock=mdata['stock']
                )
                db.session.add(m)
        db.session.commit()

        # 8. Seed Prescriptions & Dispensed Records across patients
        if not Prescription.query.first():
            prescriptions = [
                Prescription(patient_id=all_pats['PAT1001'].id, doctor_name='Dr. Priya', medicine='Paracetamol 500mg', dosage='1 Tablet', frequency='Thrice Daily', duration='5 Days', start_date='10-08-2026'),
                Prescription(patient_id=all_pats['PAT1003'].id, doctor_name='Dr. Priya', medicine='Amlodipine 5mg', dosage='1 Tablet', frequency='Once Daily (Morning)', duration='30 Days', start_date='08-08-2026'),
                Prescription(patient_id=all_pats['PAT1005'].id, doctor_name='Dr. Rajesh', medicine='Metformin 500mg', dosage='1 Tablet', frequency='Twice Daily (With Meals)', duration='30 Days', start_date='05-08-2026'),
                Prescription(patient_id=all_pats['PAT1010'].id, doctor_name='Dr. Rajesh', medicine='Sumatriptan 50mg', dosage='1 Tablet', frequency='As needed for pain', duration='10 Days', start_date='02-08-2026')
            ]
            db.session.add_all(prescriptions)
            db.session.commit()

        # 9. Seed Lab Reports across patients
        if not LabReport.query.first():
            lab_reports = [
                LabReport(patient_id=all_pats['PAT1001'].id, test_name='Complete Blood Count (CBC)', result='Normal', report_file='report_cbc_1001.pdf', test_date='10-08-2026'),
                LabReport(patient_id=all_pats['PAT1002'].id, test_name='Lipid Profile Test', result='Pending', report_file='report_lipid_1002.pdf', test_date='10-08-2026'),
                LabReport(patient_id=all_pats['PAT1003'].id, test_name='Kidney Function Test (KFT)', result='Normal', report_file='report_kft_1003.pdf', test_date='08-08-2026'),
                LabReport(patient_id=all_pats['PAT1005'].id, test_name='Fasting Blood Sugar & HbA1c', result='Critical', report_file='report_hba1c_1005.pdf', test_date='05-08-2026'),
                LabReport(patient_id=all_pats['PAT1007'].id, test_name='Lipid Profile Test', result='Borderline', report_file='report_lipid_1007.pdf', test_date='03-08-2026')
            ]
            db.session.add_all(lab_reports)
            db.session.commit()

        # 10. Seed Bills across patients
        if not Bill.query.first():
            bills = [
                Bill(invoice_number='INV-2026-0001', patient_id=all_pats['PAT1001'].id, consultation_charges=500.0, laboratory_charges=350.0, medicine_charges=35.0, subtotal=885.0, gst_rate=18.0, gst_amount=159.30, total_amount=1044.30, payment_method='UPI', payment_status='Paid', paid_at=datetime.datetime.utcnow()),
                Bill(invoice_number='INV-2026-0002', patient_id=all_pats['PAT1002'].id, consultation_charges=500.0, laboratory_charges=250.0, medicine_charges=12.0, subtotal=762.0, gst_rate=18.0, gst_amount=137.16, total_amount=899.16, payment_method='Cash', payment_status='Pending'),
                Bill(invoice_number='INV-2026-0003', patient_id=all_pats['PAT1005'].id, consultation_charges=700.0, laboratory_charges=600.0, medicine_charges=180.0, subtotal=1480.0, gst_rate=18.0, gst_amount=266.40, total_amount=1746.40, payment_method='Card', payment_status='Paid', paid_at=datetime.datetime.utcnow())
            ]
            db.session.add_all(bills)
            db.session.commit()

        print("Database initialized and populated with 10 distinct, realistic patient records and linked clinical data in MySQL!")

if __name__ == '__main__':
    seed_database()
