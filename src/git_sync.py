"""Синхронизировать проект с github."""

import os


def main() -> None:
    print("-> Синхронизация проекта с Github")
    os.system(
        "git fetch origin && git reset --hard origin/main && git clean -f -d"
    )
    print("-> Проект синхронизирован")
