from datetime import datetime
from time import sleep

from airflow import DAG
from airflow.operators.python import PythonOperator
from pendulum import timezone


def sleep_for(seconds: int) -> None:
    print(f"Oi, vou dormir agora por {seconds} segundos.")
    sleep(seconds)
    print("Agora acordei!")


with DAG(
    dag_id="demo001",
    schedule_interval="@daily",
    start_date=datetime(2023, 10, 1, tzinfo=timezone("America/Sao_Paulo")),
    catchup=False,
    default_args={
        "owner": "rodrigo",
    },
) as dag:
    start = PythonOperator(
        task_id="start", python_callable=sleep_for, op_kwargs={"seconds": 10}
    )

    start1 = PythonOperator(
        task_id="start1", python_callable=sleep_for, op_kwargs={"seconds": 5}
    )

    start2 = PythonOperator(
        task_id="start2", python_callable=sleep_for, op_kwargs={"seconds": 7}
    )

    stop = PythonOperator(
        task_id="stop",
        python_callable=sleep_for,
        op_args=[5],
    )
    one_more = PythonOperator(
        task_id="one_more", python_callable=sleep_for, op_kwargs={"seconds": 13}
    )

    start.set_downstream(one_more)
    start1.set_downstream(one_more)
    start2.set_downstream(one_more)

    stop.set_upstream(one_more)
