-- Daily enrollment
SELECT 
    trial_id,
    enrollment_date,
    COUNT(*) AS daily_enrollment
FROM enrollment
GROUP BY trial_id, enrollment_date;

-- Cumulative + velocity
WITH daily AS (
    SELECT trial_id, enrollment_date, COUNT(*) AS daily_count
    FROM enrollment
    GROUP BY trial_id, enrollment_date
),
cumulative AS (
    SELECT 
        trial_id,
        enrollment_date,
        daily_count,
        SUM(daily_count) OVER (
            PARTITION BY trial_id ORDER BY enrollment_date
        ) AS cumulative_enrollment
    FROM daily
)
SELECT *,
    cumulative_enrollment - LAG(cumulative_enrollment)
    OVER (PARTITION BY trial_id ORDER BY enrollment_date) AS velocity
FROM cumulative;

-- Site ranking
SELECT 
    site_id,
    trial_id,
    COUNT(*) AS total_enrollments,
    DENSE_RANK() OVER (
        PARTITION BY trial_id 
        ORDER BY COUNT(*) DESC
    ) AS site_rank
FROM enrollment
GROUP BY site_id, trial_id;

-- Dropout analysis
SELECT 
    trial_id,
    reason,
    COUNT(*) AS total_dropouts
FROM dropouts
GROUP BY ROLLUP(trial_id, reason);

-- Event rate
SELECT 
    e.trial_id,
    e.trial_arm,
    COUNT(a.event_id) AS total_events,
    COUNT(a.event_id) * 1.0 / COUNT(e.patient_id) AS event_rate
FROM enrollment e
LEFT JOIN adverse_events a
ON e.patient_id = a.patient_id
GROUP BY e.trial_id, e.trial_arm;

-- Dropout rate
SELECT 
    t.trial_id,
    COUNT(DISTINCT d.patient_id) * 1.0 / COUNT(DISTINCT e.patient_id) AS dropout_rate
FROM trials t
LEFT JOIN enrollment e ON t.trial_id = e.trial_id
LEFT JOIN dropouts d ON t.trial_id = d.trial_id
GROUP BY t.trial_id;