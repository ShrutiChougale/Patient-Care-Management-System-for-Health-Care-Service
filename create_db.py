from app import app
from models.models import db, Appointment

with app.app_context():
    db.create_all()
    print("Database synced with new models.")
