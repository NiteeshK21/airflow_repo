FROM apache/airflow:2.9.3

# Install dbt-core and dbt-snowflake as the airflow user
USER airflow
RUN pip install --no-cache-dir dbt-core dbt-snowflake
