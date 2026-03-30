# Local Airflow Repository

This repository contains a simple local Airflow setup with a `hello_world_dag`.

## Getting Started

1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install Airflow:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the Airflow Database:
   ```bash
   export AIRFLOW_HOME=$(pwd)
   airflow db migrate
   ```
4. Create an admin user:
   ```bash
   airflow users create \
       --username admin \
       --firstname Admin \
       --lastname User \
       --role Admin \
       --email admin@example.com
   ```
5. Start the web server in detached mode:
   ```bash
   airflow webserver --port 8080 -D
   ```
6. Start the scheduler in detached mode:
   ```bash
   airflow scheduler -D
   ```

You can now visit http://localhost:8080 and log in with the admin credentials you created to see and trigger the `hello_world_dag`.
