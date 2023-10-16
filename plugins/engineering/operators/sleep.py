from typing import Any
from airflow.models.baseoperator import BaseOperator
from airflow.utils.context import Context
from time import sleep

class SleepOperator(BaseOperator):

    ui_color = "#052DE5"
    ui_fgcolor = "#ffffff"
    def __init__(self, sleep_for_seconds: int, **kwargs):
        super().__init__(**kwargs)
        self.__sleep_for_seconds = sleep_for_seconds


    def execute(self, context: Context) -> Any:
        self.log.info("Dormindo por %s", self.__sleep_for_seconds)
        sleep(self.__sleep_for_seconds)
