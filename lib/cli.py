import click
from db.models import Session, Patient, Doctor, Appointment
from datetime import datetime

session = Session()

@click.group()
def cli():
    pass

def manage_patients():
    """Manage patients: add, delete, list, admit, release, schedule appointment."""
    while True:
        click.echo("Choose an action:")
        click.echo("1: Add Patient")
        click.echo("2: Delete Patient")
        click.echo("3: List Patients")
        click.echo("4: Admit Patient")
        click.echo("5: Release Patient")
        click.echo("6: Schedule Appointment")
        click.echo("7: Exit")

        choice = click.prompt("Enter the number of your choice", type=int)
        click.echo(f'You chose: {choice}')  # Debug output

        if choice == 1:
            name = click.prompt("Enter patient's name")
            age = click.prompt("Enter patient's age", type=int)
            add_patient(name, age)
        elif choice == 2:
            patient_id = click.prompt("Enter patient ID", type=int)
            delete_patient(patient_id)
        elif choice == 3:
            list_patients()
        elif choice == 4:
            patient_id = click.prompt("Enter patient ID", type=int)
            admit_patient(patient_id)
        elif choice == 5:
            patient_id = click.prompt("Enter patient ID", type=int)
            prescription = click.prompt("Enter prescription")
            release_patient(patient_id, prescription)
        elif choice == 6:
            doctor_id = click.prompt("Enter doctor name ", type=str)
            patient_id = click.prompt("Enter patient name", type=str)
            appointment_date = click.prompt("Enter appointment date (YYYY-MM-DD)", type=str)
            schedule_appointment(doctor_id, patient_id, appointment_date)
        elif choice == 7:
            click.echo("Goodbye come back again.....")
            break
        else:
            click.echo("Invalid choice.Please try again.")

def add_patient(name, age):
    """Add a new patient."""
    try:
        patient = Patient(name=name, age=int(age), status='admitted')
        session.add(patient)
        session.commit()
        click.echo(f' {name}  has been added and admitted to the system .')
    except Exception as e:
        click.echo(f'Error adding patient: {e}')

def delete_patient(patient_id):
    """Delete a patient."""
    try:
        patient = session.query(Patient).get(patient_id)
        if patient:
            session.delete(patient)
            session.commit()
            click.echo(f' {patient.name} has been deleted from the medical systems.')
        else:
            click.echo('Patient not found.')
    except Exception as e:
        click.echo(f'Error deleting patient: {e}')

def list_patients():
    """List all patients."""
    try:
        patients = session.query(Patient).all()
        for patient in patients:
            click.echo(f'The patient id-{patient.id}, {patient.name}, {patient.age} years old is of the Status: {patient.status}')
    except Exception as e:
        click.echo(f'Error listing patients: {e}')

def admit_patient(patient_id):
    """Admit a patient."""
    try:
        patient = session.query(Patient).get(patient_id)
        if patient:
            patient.status = 'admitted'
            session.commit()
            click.echo(f'Patient {patient.name} admitted.')
        else:
            click.echo('Patient not found.')
    except Exception as e:
        click.echo(f'Error admitting patient: {e}')

def release_patient(patient_id, prescription):
    """Release a patient with a prescription."""
    try:
        patient = session.query(Patient).get(patient_id)
        if patient:
            patient.status = 'released'
            patient.prescription = prescription
            session.commit()
            click.echo(f'Patient {patient.name} released with prescription: {prescription}.')
        else:
            click.echo('Patient not found.')
    except Exception as e:
        click.echo(f'Error releasing patient: {e}')

        
def schedule_appointment(doctor_name, patient_name, appointment_date):
    """Schedule an appointment for a patient with a doctor."""
    try:
        # Query doctor and patient by name
        doctor = session.query(Doctor).filter_by(name=doctor_name).first()
        patient = session.query(Patient).filter_by(name=patient_name).first()

        if doctor and patient:
            appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d")
            appointment = Appointment(doctor_id=doctor.id, patient_id=patient.id, date=appointment_date)
            session.add(appointment)
            session.commit()
            click.echo(f'Appointment scheduled for patient {patient_name} with doctor {doctor_name} on {appointment_date.date()}.')
        else:
            click.echo('Doctor or patient not found.')
    except Exception as e:
        click.echo(f'Error scheduling appointment: {e}')

if __name__ == '__main__':
    manage_patients()