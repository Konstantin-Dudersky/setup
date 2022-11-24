"""Установка poetry."""

import logging
import os
from typing import Callable, Iterable

from .internal.base_task import BaseTask
from .simple_command import SimpleCommand

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class _PoetryBase(BaseTask):
    def __init__(
        self,
        desc: str,
        dirs: Iterable[str],
        need_confirm: bool = True,
    ) -> None:
        super().__init__(desc, need_confirm)
        self._dirs = dirs


class PoetryInstall(_PoetryBase):
    """Установка пакетов."""

    def _execute(self) -> None:
        for directory in self._dirs:
            log.info("Установка в папке: {0}".format(directory))
            SimpleCommand(
                desc="Установка окружения poetry",
                command="poetry install",
                need_confirm=False,
                work_dir_rel=directory,
            ).execute()


class PoetryRemove(_PoetryBase):
    """Удалить виртуальные окружения."""

    def _execute(self) -> None:
        for directory in self._dirs:
            log.info("Удалить в папке: {0}".format(directory))
            SimpleCommand(
                desc="Удаление окружения poetry",
                command="poetry env remove --all",
                need_confirm=False,
                work_dir_rel=directory,
            ).execute()


class PoetryUpdate(_PoetryBase):
    """Обновление пакетов."""

    def _execute(self) -> None:
        for directory in self._dirs:
            log.info("Обновить в папке: {0}".format(directory))
            SimpleCommand(
                desc="Обновление окружения poetry",
                command="poetry update",
                need_confirm=False,
                work_dir_rel=directory,
            ).execute()


class PoetryShowOutdated(_PoetryBase):
    """Проверка устаревших пакетов."""

    def _execute(self) -> None:
        for directory in self._dirs:
            log.info(
                "Проверка устаревших пакетов в папке: {0}".format(directory),
            )
            SimpleCommand(
                desc="Проверка устаревших пакетов",
                command="poetry show -o",
                need_confirm=False,
                work_dir_rel=directory,
            ).execute()


# obsolete ---------------------------------------------------------------------


def poetry_self_install(version: str = "1.1.14") -> Callable[[], None]:
    """Entry point."""

    def _main() -> None:
        os.system("sudo apt update")
        os.system("sudo apt install -y python3-venv curl")
        os.system(
            "curl -sSL https://install.python-poetry.org"
            f" | python3 - --version {version}"
        )
        print(
            """-> Если следующая команда выполняется с ошибкой
-> Command 'poetry' not found
-> нужно добавить в файл .bashrc
-> export PATH="$HOME/.local/bin:$PATH"
"""
        )
        os.system(". ~/.profile && poetry config virtualenvs.in-project true")

    return _main


def poetry_self_update(version: str = "1.1.14") -> Callable[[], None]:
    """Entry point."""

    def _main() -> None:
        os.system(f"poetry self update {version}")

    return _main
