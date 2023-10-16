"""
# DAG demo ingestão blablabla

shudsfhduif fduihfduihfgui fi ghjuihbuifui hfui
firfhguituit
jrtuighuithbti

> Cuidado com essa dag.


"""
from random import randint

from airflow import DAG
from airflow.operators.empty import EmptyOperator

from engineering.operators.sleep import SleepOperator
from engineering.utils.date import days_ago


with DAG(
    dag_id="demo002",
    schedule_interval="@daily",
    start_date=days_ago(10),
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "rodrigo"},
) as dag:
    tasks = {
        "start": EmptyOperator(task_id="start"),
        "stop": EmptyOperator(task_id="stop"),
    }

    for index in range(1, 11):
        task_id = f"task_{str(index).zfill(3)}"

        tasks[task_id] = SleepOperator(
            task_id=task_id,
            sleep_for_seconds=randint(5, 30),
        )
        tasks[task_id].set_upstream(tasks["start"])
        tasks[task_id].set_downstream(tasks["stop"])
