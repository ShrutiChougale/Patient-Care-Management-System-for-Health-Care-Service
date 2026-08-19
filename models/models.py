from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from sqlalchemy.orm import validates

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'userss'
    __table_args__ = (
        db.Index('idx_user_email', 'email'),
        db.Index('idx_user_role', 'role'),
    )
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='Patient') # Admin, Doctor, Nurse, Pharmacist, Laboratory Staff, Patient

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Patient(db.Model):
    __tablename__ = 'patients'
    __table_args__ = (
        db.Index('idx_patient_code', 'patient_code'),
        db.Index('idx_patient_email', 'email'),
        db.Index('idx_patient_phone', 'phone_number'),
        db.Index('idx_patient_aadhaar', 'aadhaar_number'),
    )
    id = db.Column(db.Integer, primary_key=True)
    patient_code = db.Column(db.String(20), unique=True, nullable=False, default='PAT1001')
    full_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.Text, nullable=False)
    blood_group = db.Column(db.String(5), nullable=False)
    aadhaar_number = db.Column(db.String(12), unique=True, nullable=False)
    date_of_birth = db.Column(db.String(20), nullable=True)
    medical_history = db.Column(db.Text, nullable=True)

    @validates('aadhaar_number')
    def validate_aadhaar_number(self, key, value):
        if not value:
            raise ValueError("Aadhaar number is required and cannot be empty.")
        clean_val = str(value).replace(' ', '').replace('-', '').strip()
        if not clean_val or not clean_val.isdigit() or len(clean_val) != 12:
            raise ValueError("Aadhaar number must be exactly 12 numeric digits.")
        return clean_val

    @property
    def masked_aadhaar(self):
        if not self.aadhaar_number or len(self.aadhaar_number) != 12:
            return "N/A"
        return f"XXXX-XXXX-{self.aadhaar_number[-4:]}"
    
    # EHR Medical Summary fields
    height = db.Column(db.String(20), default='175 cm')
    weight = db.Column(db.String(20), default='72 kg')
    bmi = db.Column(db.String(20), default='23.5')
    smoking = db.Column(db.String(20), default='No')
    alcohol = db.Column(db.String(20), default='Occasional')
    chronic_diseases = db.Column(db.String(100), default='No')
    remarks = db.Column(db.Text, default='Patient is healthy.')

    # Relationships
    appointments = db.relationship('Appointment', backref='patient', lazy=True, cascade='all, delete-orphan')
    consultations = db.relationship('Consultation', backref='patient', lazy=True, cascade='all, delete-orphan')
    prescriptions = db.relationship('Prescription', backref='patient', lazy=True, cascade='all, delete-orphan')
    lab_reports = db.relationship('LabReport', backref='patient', lazy=True, cascade='all, delete-orphan')
    allergies = db.relationship('Allergy', backref='patient', lazy=True, cascade='all, delete-orphan')
    diagnoses = db.relationship('Diagnosis', backref='patient', lazy=True, cascade='all, delete-orphan')
    dispensed_medicines = db.relationship('DispensedMedicine', backref='patient', lazy=True, cascade='all, delete-orphan')
    bills = db.relationship('Bill', backref='patient', lazy=True, cascade='all, delete-orphan')
    feedbacks = db.relationship('PatientFeedback', backref='patient', lazy=True, cascade='all, delete-orphan')

class Doctor(db.Model):
    __tablename__ = 'doctors'
    __table_args__ = (
        db.Index('idx_doctor_email', 'email_address'),
        db.Index('idx_doctor_dept', 'department'),
    )
    id = db.Column(db.Integer, primary_key=True)
    doctor_name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    qualification = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    available_time = db.Column(db.String(100), nullable=False)

    appointments = db.relationship('Appointment', backref='doctor', lazy=True)
    consultations = db.relationship('Consultation', backref='doctor', lazy=True)
    feedbacks = db.relationship('PatientFeedback', backref='doctor', lazy=True)

class Appointment(db.Model):
    __tablename__ = 'appointments'
    __table_args__ = (
        db.Index('idx_app_patient_id', 'patient_id'),
        db.Index('idx_app_doctor_id', 'doctor_id'),
        db.Index('idx_app_date_status', 'appointment_date', 'status'),
    )
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(50), default='Scheduled') # Scheduled, Completed, Cancelled

class Consultation(db.Model):
    __tablename__ = 'consultations'
    __table_args__ = (
        db.Index('idx_cons_patient_id', 'patient_id'),
        db.Index('idx_cons_doctor_id', 'doctor_id'),
        db.Index('idx_cons_created_at', 'created_at'),
    )
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=True)
    doctor_name = db.Column(db.String(100), nullable=False, default='Dr. Priya')
    consultation_date = db.Column(db.String(20), nullable=False, default=lambda: datetime.now().strftime('%d-%m-%Y'))
    symptoms = db.Column(db.Text, nullable=False)
    diagnosis = db.Column(db.String(255), nullable=False)
    treatment_prescription = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Prescription(db.Model):
    __tablename__ = 'prescriptions'
    __table_args__ = (
        db.Index('idx_presc_patient_id', 'patient_id'),
        db.Index('idx_presc_created_at', 'created_at'),
    )
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_name = db.Column(db.String(100), nullable=False, default='Dr. Priya')
    medicine = db.Column(db.String(150), nullable=False)
    dosage = db.Column(db.String(50), nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.String(50), nullable=False, default='5 Days')
    start_date = db.Column(db.String(20), nullable=False, default=lambda: datetime.now().strftime('%d-%m-%Y'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class LabReport(db.Model):
    __tablename__ = 'lab_reports'
    __table_args__ = (
        db.Index('idx_lab_patient_id', 'patient_id'),
        db.Index('idx_lab_result', 'result'),
        db.Index('idx_lab_created_at', 'created_at'),
    )
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    test_name = db.Column(db.String(150), nullable=False)
    test_date = db.Column(db.String(20), nullable=False, default=lambda: datetime.now().strftime('%d-%m-%Y'))
    result = db.Column(db.String(50), nullable=False, default='Pending') # Pending, Normal, Borderline, Critical
    report_file = db.Column(db.String(255), nullable=True, default='report.pdf')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Allergy(db.Model):
    __tablename__ = 'allergies'
    __table_args__ = (
        db.Index('idx_allergy_patient_id', 'patient_id'),
    )
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    allergen = db.Column(db.String(100), nullable=False)
    reaction = db.Column(db.String(100), nullable=False)
    added_on = db.Column(db.String(20), nullable=False, default=lambda: datetime.now().strftime('%d-%m-%Y'))

class Diagnosis(db.Model):
    __tablename__ = 'diagnoses'
    __table_args__ = (
        db.Index('idx_diag_patient_id', 'patient_id'),
    )
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    diagnosis_date = db.Column(db.String(20), nullable=False)
    diagnosis_name = db.Column(db.String(150), nullable=False)
    doctor_name = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text, nullable=True)

class Medicine(db.Model):
    __tablename__ = 'medicines'
    __table_args__ = (
        db.Index('idx_med_code', 'medicine_code'),
        db.Index('idx_med_name', 'name'),
        db.Index('idx_med_exp_date', 'exp_date'),
    )
    id = db.Column(db.Integer, primary_key=True)
    medicine_code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    manufacturer = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    batch_number = db.Column(db.String(50), nullable=False)
    mfg_date = db.Column(db.Date, nullable=False)
    exp_date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float, nullable=False, default=0.0)
    stock = db.Column(db.Integer, nullable=False, default=0)
    min_stock_alert = db.Column(db.Integer, default=10)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    dispensed_records = db.relationship('DispensedMedicine', backref='medicine', lazy=True, cascade='all, delete-orphan')

class DispensedMedicine(db.Model):
    __tablename__ = 'dispensed_medicines'
    __table_args__ = (
        db.Index('idx_disp_patient_id', 'patient_id'),
        db.Index('idx_disp_medicine_id', 'medicine_id'),
        db.Index('idx_disp_at', 'dispensed_at'),
    )
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.id'), nullable=False)
    pharmacist_name = db.Column(db.String(100), nullable=False, default='System Pharmacist')
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    dispensed_at = db.Column(db.DateTime, default=datetime.utcnow)

class Bill(db.Model):
    __tablename__ = 'bills'
    __table_args__ = (
        db.Index('idx_bill_inv', 'invoice_number'),
        db.Index('idx_bill_patient_id', 'patient_id'),
        db.Index('idx_bill_status', 'payment_status'),
    )
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(30), unique=True, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    consultation_charges = db.Column(db.Float, default=0.0)
    laboratory_charges = db.Column(db.Float, default=0.0)
    medicine_charges = db.Column(db.Float, default=0.0)
    additional_charges = db.Column(db.Float, default=0.0)
    room_charges = db.Column(db.Float, default=0.0)
    subtotal = db.Column(db.Float, nullable=False, default=0.0)
    gst_rate = db.Column(db.Float, default=18.0)
    gst_amount = db.Column(db.Float, nullable=False, default=0.0)
    total_amount = db.Column(db.Float, nullable=False, default=0.0)
    payment_method = db.Column(db.String(30), nullable=False, default='Cash') # Cash, UPI, Card, Net Banking
    payment_status = db.Column(db.String(20), nullable=False, default='Pending') # Pending, Paid, Failed
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    paid_at = db.Column(db.DateTime, nullable=True)

class Notification(db.Model):
    __tablename__ = 'notifications'
    __table_args__ = (
        db.Index('idx_notif_role', 'recipient_role'),
        db.Index('idx_notif_user', 'recipient_user_id'),
        db.Index('idx_notif_status', 'status'),
    )
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='unread') # unread, read, delivered
    recipient_role = db.Column(db.String(50), default='all') # all, Doctor, Patient, Nurse, Pharmacist, Laboratory Staff
    recipient_user_id = db.Column(db.Integer, db.ForeignKey('userss.id'), nullable=True)
    notification_type = db.Column(db.String(50), nullable=False) # Appointment Reminder, Prescription Ready, Lab Report Ready, Billing Reminder, Hospital Announcement

class LoginLog(db.Model):
    __tablename__ = 'login_logs'
    __table_args__ = (
        db.Index('idx_log_user_id', 'user_id'),
        db.Index('idx_log_time', 'login_time'),
    )
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('userss.id'), nullable=True)
    user_email = db.Column(db.String(120), nullable=False)
    ip_address = db.Column(db.String(50), nullable=False, default='127.0.0.1')
    login_time = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False) # Success, Failed
    user_agent = db.Column(db.String(255), nullable=True)

class SupportTicket(db.Model):
    __tablename__ = 'support_tickets'
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Open') # Open, In Progress, Closed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Milestone 4: Patient Feedback Model
class PatientFeedback(db.Model):
    __tablename__ = 'patient_feedbacks'
    __table_args__ = (
        db.Index('idx_fb_patient_id', 'patient_id'),
        db.Index('idx_fb_doctor_id', 'doctor_id'),
        db.Index('idx_fb_rating', 'rating'),
    )
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=True)
    rating = db.Column(db.Integer, nullable=False) # 1 to 5 stars
    comments = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)