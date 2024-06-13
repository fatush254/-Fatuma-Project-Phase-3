# lib/db/models.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# Association table for many-to-many relationship between Patient and Doctor
patient_doctor_association = Table(
    'patient_doctor_association', Base.metadata,
    Column('patient_id', Integer, ForeignKey('patients.id')),
    Column('doctor_id', Integer, ForeignKey('doctors.id'))
)

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    status = Column(String)  # New field for admission status
    prescription = Column(String)  # New field for prescription upon release
    doctors = relationship('Doctor', secondary=patient_doctor_association, back_populates='patients')
    appointments = relationship('Appointment', back_populates='patient')

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialty = Column(String)
    patients = relationship('Patient', secondary=patient_doctor_association, back_populates='doctors')
    appointments = relationship('Appointment', back_populates='doctor')

class Appointment(Base)
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient_id = Column(Integer, ForeignKey('patients.id'))
    date = Column(DateTime)

    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")



engine = create_engine('sqlite:///medical_record_system.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)