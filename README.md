# Cybersecurity Incident Tracker

Aspiring Data Analyst project to parse, analyze, and query cybersecurity incident logs.

## Purpose
Tracks cybersecurity incidents from a log file, analyzes them with NumPy, and stores/queries them in SQLite. Built to practice data parsing, numerical analysis, and database skills for cybersecurity applications.

## Data Used
Simulated incidents.txt with columns: date, time, incident_type, ip_address, severity_rating, target_system—created manually.

## Approach
- *Parser (incident_parser.py)*: Reads incidents.txt, splits lines into a list of 6-column rows.
- *NumPy Analysis (incident_np.py)*: Converts list to array, calculates total incidents, average severity, unique IPs.
- *SQL (incident_sql.py)*: Stores raw data in incidents.db with transactions (commit/rollback), displays table with tabulate, runs user-input SELECT queries.

## Results
Parsed incidents, computed stats (e.g., avg severity 3.2, 4 unique IPs), stored in SQLite with transaction safety, and queried dynamically (e.g., 5 Failed Logins) with tabulated output.

## Tools Used
- Python
- NumPy
- SQLite (sqlite3)
- tabulate (for clean table display)

## How to Run
1. Clone the repo
2. Install dependencies: pip install numpy tabulate
3. Run analysis: python incident_np.py
4. Run SQL tool: python incident_sql.py (interactively query incidents.db)

## Files
- incident_parser.py: Parses incidents.txt.
- incident_np.py: Analyzes data with NumPy.
- incident_sql.py: Stores and queries data in SQLite.
- incidents.txt: Sample log file.