from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from pendulum import datetime


@dag(start_date=datetime(2024, 8, 15), schedule=None, catchup=False)
def dbt_bigquery_models_dag():
    execute_my_script = BashOperator(
        task_id="execute_dbt_script",
        bash_command="$AIRFLOW_HOME/dags/scripts/script.sh ",
    
    )

    execute_my_script


dbt_bigquery_models_dag()