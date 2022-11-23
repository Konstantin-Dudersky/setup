"""Синхронизация кода."""

import logging
import subprocess
from typing import Final

from .internal.base_task import BaseTask

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

CMD: Final[str] = (
    "rsync -vhra . {remote_path} --include='**.gitignore' --exclude='/.git' "
    + "--filter=':- .gitignore' --delete-after"
)


class CodeSync(BaseTask):
    """Синхронизация кода."""

    def __init__(
        self,
        desc: str,
        need_confirm: bool = True,
        remote_path: str = "user@target:/destination/project/",
    ) -> None:
        """Базовый класс для задачи.

        Parameters
        ----------
        desc: str
            Описание задачи
        need_confirm: bool
            Требуется подтверждение запуска
        remote_path: str
            ssh-путь на удаленной машине
        """
        super().__init__(desc, need_confirm)
        self.__remote_path = remote_path

    def _execute(self) -> None:
        subprocess.run(
            CMD.format(
                remote_path=self.__remote_path,
            ).split(),
        )
