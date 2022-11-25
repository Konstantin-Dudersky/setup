"""Запуск задач."""

import logging
from typing import List, NamedTuple

from ._shared import get_logger
from ..internal.base_task import BaseTask
from ..internal.compose_task import ComposeTask


log = get_logger(__name__, logging.DEBUG)


class Runner(object):
    """Основной класс для запуска."""

    def __init__(
        self,
        args: List[str],
        simple_tasks: NamedTuple,
        compose_tasks: NamedTuple,
    ) -> None:
        """Основной класс для запуска."""
        self.__args = args
        self.__simple_tasks = simple_tasks
        self.__compose_tasks = compose_tasks

        self.__save_task_names()
        if len(self.__args) <= 1:
            self.__print()
            return
        task_name = self.__args[1]
        if self.__try_start_simple_task(task_name):
            return
        if self.__try_start_compose_task(task_name):
            return
        log.error("Задача {0} не найдена!".format(task_name))

    def __save_task_names(self):
        task: BaseTask
        for task_name, task in self.__simple_tasks._asdict().items():
            task.name = task_name
        compose_task: ComposeTask
        for (
            complse_task_name,
            compose_task,
        ) in self.__compose_tasks._asdict().items():
            compose_task.name = complse_task_name

    def __print(self) -> None:
        log.debug("\nЗадачи:")
        for st in self.__simple_tasks:
            log.debug("* {0}".format(st))
        log.debug("\nКомбинированные задачи:")
        for ct in self.__compose_tasks:
            log.debug(ct)

    def __try_start_simple_task(self, task_name: str) -> bool:
        if task_name not in self.__simple_tasks._asdict().keys():
            return False
        simple_task: BaseTask = self.__simple_tasks._asdict()[task_name]
        simple_task.execute()
        return True

    def __try_start_compose_task(self, task_name: str) -> bool:
        if task_name not in self.__compose_tasks._asdict().keys():
            return False
        compose_tasks: ComposeTask = self.__compose_tasks._asdict()[task_name]
        compose_tasks.execute()
        return True
