CREATE TABLE trials (
    trial_id SERIAL PRIMARY KEY,
    trial_name TEXT,
    phase TEXT,
    target_enrollment INT,
    start_date DATE,
    end_date DATE
);

CREATE TABLE sites (
    site_id SERIAL PRIMARY KEY,
    site_name TEXT,
    country TEXT
);

CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    age INT,
    gender TEXT
);

CREATE TABLE enrollment (
    enrollment_id SERIAL PRIMARY KEY,
    trial_id INT REFERENCES trials(trial_id),
    site_id INT REFERENCES sites(site_id),
    patient_id INT REFERENCES patients(patient_id),
    enrollment_date DATE,
    trial_arm TEXT
);

CREATE TABLE visits (
    visit_id SERIAL PRIMARY KEY,
    patient_id INT,
    visit_date DATE,
    visit_type TEXT
);

CREATE TABLE adverse_events (
    event_id SERIAL PRIMARY KEY,
    patient_id INT,
    trial_id INT,
    severity TEXT,
    event_date DATE
);

CREATE TABLE dropouts (
    dropout_id SERIAL PRIMARY KEY,
    patient_id INT,
    trial_id INT,
    dropout_date DATE,
    reason TEXT
);