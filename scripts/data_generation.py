import random
import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()

print("Setup successful!")

# TRIALS 
trials = pd.DataFrame({
    "trial_id": [1, 2, 3],
    "trial_name": ["Oncology Study A", "Diabetes Study B", "Cardio Study C"],
    "phase": ["Phase III", "Phase II", "Phase III"],
    "target_enrollment": [300, 200, 250],
    "start_date": pd.to_datetime(["2025-01-01", "2025-02-01", "2025-03-01"])
})

print("\nTrials Data:")
print(trials.head())

# SITES 
sites = pd.DataFrame({
    "site_id": range(1, 11),
    "site_name": [fake.company() for _ in range(10)],
    "country": random.choices(
        ["USA", "India", "UK", "Germany", "Canada"],
        k=10
    )
})

print("\nSites Sample:")
print(sites.head())

# PATIENTS 
num_patients = 500

patients = pd.DataFrame({
    "patient_id": range(1, num_patients + 1),
    "age": np.random.randint(18, 80, num_patients),
    "gender": random.choices(["Male", "Female"], k=num_patients)
})

print("\nPatients Sample:")
print(patients.head())
print("Total Patients:", len(patients))

# ENROLLMENT 
enrollment_data = []

for patient_id in patients["patient_id"]:
    
    trial_id = random.choice([1, 2, 3])
    
    site_id = np.random.choice(
        sites["site_id"],
        p=[0.15,0.15,0.1,0.1,0.1,0.1,0.1,0.1,0.05,0.05]
    )
    
    base_date = pd.to_datetime("2025-01-01")
    enrollment_date = base_date + pd.Timedelta(days=np.random.randint(0, 180))
    
    trial_arm = random.choice(["Control", "Drug A", "Drug B"])
    
    enrollment_data.append([
        patient_id,
        trial_id,
        site_id,
        enrollment_date,
        trial_arm
    ])

enrollment = pd.DataFrame(enrollment_data, columns=[
    "patient_id", "trial_id", "site_id", "enrollment_date", "trial_arm"
])

print("\nEnrollment Sample:")
print(enrollment.head())
print("Total Enrollments:", len(enrollment))

# DROPOUTS 
dropout_reasons = [
    "Side Effects",
    "Lost to Follow-up",
    "Personal Reasons",
    "Protocol Violation"
]

dropouts = enrollment.sample(frac=0.2).copy()

dropouts["dropout_date"] = dropouts["enrollment_date"] + pd.to_timedelta(
    np.random.randint(10, 60, len(dropouts)), unit="D"
)

dropouts["reason"] = random.choices(dropout_reasons, k=len(dropouts))

dropouts = dropouts[["patient_id", "trial_id", "dropout_date", "reason"]]

print("\nDropouts Sample:")
print(dropouts.head())
print("Total Dropouts:", len(dropouts))

# ADVERSE EVENTS 
adverse_events = enrollment.sample(frac=0.3).copy()

adverse_events["severity"] = random.choices(
    ["Mild", "Moderate", "Severe"],
    weights=[0.5, 0.3, 0.2],
    k=len(adverse_events)
)

adverse_events["event_date"] = adverse_events["enrollment_date"] + pd.to_timedelta(
    np.random.randint(5, 50, len(adverse_events)), unit="D"
)

adverse_events = adverse_events[
    ["patient_id", "trial_id", "severity", "event_date"]
]

print("\nAdverse Events Sample:")
print(adverse_events.head())
print("Total Events:", len(adverse_events))

# SAVE FILES 
trials.to_csv("trials.csv", index=False)
sites.to_csv("sites.csv", index=False)
patients.to_csv("patients.csv", index=False)
enrollment.to_csv("enrollment.csv", index=False)
dropouts.to_csv("dropouts.csv", index=False)
adverse_events.to_csv("adverse_events.csv", index=False)

print("\nAll CSV files saved successfully!")