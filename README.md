# setup

Скрипты установки

```sh
sudo chmod +x src/python.py && ./src/python.py 3.10.5 # установка нужной версии python
sudo chmod +x src/poetry.py && ./src/poetry.py # установка poetry
poetry install --no-dev
poetry run poe port_redirect # проброс портов с 8000 на 80
```

## systemd

Для запуска systemd сервиса нужно задать задачу poe в файле pyproject.toml

```sh
[tool.poe.tasks]
systemd = {script = "src.systemd:main(service_name='<service_name>', description='<description>', work_dir_rel='<work_dir_rel>'"}
```

work_dir_rel - относительный путь к рабочей папке сервиса

После создания задачи генерацию файла можно запустить:

```sh
poetry run poe systemd
```

## port_redirect

Перенаправление портов, поскольку на linux нельзя запусить сервис с портом <= 1024

```sh
# TODO
```



## angular

### сборка проекта

```sh
[tool.poe.tasks]
ng_build = {script = "src.ng_build:main(work_dir_relative='../client', project='client')"}
```

