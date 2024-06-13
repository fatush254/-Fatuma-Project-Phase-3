# lib/db/app.py

from models import Session, Patient, Doctor

def seed_data():
    session = Session()

    # Sample patients
    patient1 = Patient(name='John Doe', age=30, status='admitted')
    patient2 = Patient(name='Jane Smith', age=25, status='admitted')

    # Sample doctors
    doctor1 = Doctor(name='Dr. Brown', specialty='Cardiology')
    doctor2 = Doctor(name='Dr. Green', specialty='Neurology')

    session.add_all([patient1, patient2, doctor1, doctor2])
    session.commit()

    session.close()

if __name__ == '__main__':
    seed_data()