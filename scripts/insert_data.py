import psycopg2
import pandas as pd

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="clinical_trials",
    user="postgres",
    password="IlrAwb!1809!"   
)

cur = conn.cursor()

print("Connected to PostgreSQL!")

trials = pd.read_csv("trials.csv")
sites = pd.read_csv("sites.csv")
patients = pd.read_csv("patients.csv")
enrollment = pd.read_csv("enrollment.csv")
dropouts = pd.read_csv("dropouts.csv")
adverse_events = pd.read_csv("adverse_events.csv")

print("CSV files loaded successfully!")

# Trial 

for _, row in trials.iterrows():
    cur.execute("""
        INSERT INTO trials (trial_id, trial_name, phase, target_enrollment, start_date)
        VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
print("Trials inserted!")

# Sites

for _, row in sites.iterrows():
    cur.execute("""
        INSERT INTO sites (site_id, site_name, country)
        VALUES (%s, %s, %s)
    """, tuple(row))

conn.commit()
print("Sites inserted!")

# Patients 

for _, row in patients.iterrows():
    cur.execute("""
        INSERT INTO patients (patient_id, age, gender)
        VALUES (%s, %s, %s)
    """, tuple(row))

conn.commit()
print("Patients inserted!")

#Enrollment

for _, row in enrollment.iterrows():
    cur.execute("""
        INSERT INTO enrollment (patient_id, trial_id, site_id, enrollment_date, trial_arm)
        VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
print("Enrollment inserted!")

# Dropout 

for _, row in dropouts.iterrows():
    cur.execute("""
        INSERT INTO dropouts (patient_id, trial_id, dropout_date, reason)
        VALUES (%s, %s, %s, %s)
    """, tuple(row))

conn.commit()
print("Dropouts inserted!")

# Adverse Events 

for _, row in adverse_events.iterrows():
    cur.execute("""
        INSERT INTO adverse_events (patient_id, trial_id, severity, event_date)
        VALUES (%s, %s, %s, %s)
    """, tuple(row))

conn.commit()
print("Adverse events inserted!")

cur.close()
conn.close()

print("All data inserted successfully")