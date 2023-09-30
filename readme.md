# Отчет по заданию "Идентификация и аутентификация"

## Задача

В данном задании мы выполнили следующие шаги:

1. Создали виртуальную машину на базе ОС Debian 12.
2. Создали пользователя `super-{Egorov.Y.A}` и наделили его привилегиями суперпользователя.
3. Создали группу `group-{1}`.
4. Добавили пользователя `super-{Egorov.Y.A}` в группу `group-{1}`.
5. Проверили наличие пользователя в группе.
6. Создали пользователя `user-{Egorov.Y.A}` и добавили его в группу `group-{1}`.
7. Наделили полномочиями пользователя `user-{Egorov.Y.A}` по созданию и удалению файлов в домашнем каталоге пользователя `super-{Egorov.Y.A}` с использованием механизма разграничения доступа `chmod`.
8. Продемонстрировали работу механизмов разграничения доступа.

## Шаги выполнения

```bash
# Шаг 2
root@EgorovY:~# useradd super-{Egorov.Y.A}
root@EgorovY:~# passwd super-{Egorov.Y.A}
root@EgorovY:~# usermod -aG sudo super-{Egorov.Y.A}

# Шаг 3
root@EgorovY:~# groupadd group-{1}

# Шаг 4
root@EgorovY:~# usermod -aG group-{1} super-{Egorov.Y.A}

# Шаг 5
root@EgorovY:~# groups super-{Egorov.Y.A}

# Шаг 6
root@EgorovY:~# useradd user-{Egorov.Y.A}
root@EgorovY:~# usermod -aG group-{1} user-{Egorov.Y.A}

# Шаг 7
root@EgorovY:~# chmod 770 /home/super-{Egorov.Y.A}
root@EgorovY:~# chown super-{Egorov.Y.A}:group-{1} /home/super-{Egorov.Y.A}

# Шаг 8
$ su user-{Egorov.Y.A}
$ touch /home/super-{Egorov.Y.A}/test_file.txt
$ rm /home/super-{Egorov.Y.A}/test_file.txt
