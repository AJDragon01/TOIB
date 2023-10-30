### Лабораторная работа 1: Отчет

#### Цель
Создать и настроить две виртуальные машины на базе ОС Debian 12 в среде VirtualBox, установить и настроить Keycloak, развернуть тестовое приложение и включить двухфакторную аутентификацию OTP через Keycloak.

#### Шаги выполнения

##### 1. Создание виртуальных машин
- Скачан образ ОС Debian 12.1.0 AMD64 Netinst с [сайта Debian](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.1.0-amd64-netinst.iso).
- Установлен VirtualBox версии 6.0 с [официального сайта](https://www.virtualbox.org/wiki/Downloads).
- Созданы две виртуальные машины в VirtualBox с установленной ОС Debian 12.

##### 2. Обеспечение сетевого обмена
- Настроен сетевой обмен между двумя виртуальными машинами в соответствии с инструкцией [VirtualBox Manual](https://www.virtualbox.org/manual/ch06.html).

##### 3. Установка и настройка Keycloak на ВМ 1
- Установлен Keycloak на первой виртуальной машине в соответствии с документацией [Keycloak Server Administration](https://www.keycloak.org/docs/latest/server_admin/).
- Выполнена первоначальная настройка Keycloak.
- Создан Realm.
- Добавлены пользователи "appadmin" и "user" в созданный Realm.

##### 4. Начальная настройка
- Развернуто тестовое приложение на второй виртуальной машине согласно инструкции [Introduction to IAM with Keycloak](https://kzhekov.medium.com/introduction-to-iam-with-keycloak-7b1127a16e0e).
- Настроено подключение тестового приложения к Keycloak для аутентификации и авторизации.

![Скриншот 1](https://github.com/AJDragon01/TOIB_Egorov/assets/145147455/c81addf0-87cb-442b-86b3-18131b0caca8)

![Скриншот 2](https://github.com/AJDragon01/TOIB_Egorov/assets/145147455/25b18771-252a-468d-8be6-3025452e629f)

![Скриншот 3](https://github.com/AJDragon01/TOIB_Egorov/assets/145147455/6abf82dc-fac0-4f04-b29e-abcb22dec1a3)

![Скриншот 4](https://github.com/AJDragon01/TOIB_Egorov/assets/145147455/2f3ae463-58d9-43ba-8cb6-fa5a1bf30b97)

![Скриншот 5](https://github.com/AJDragon01/TOIB_Egorov/assets/145147455/c13d9159-622b-45ba-acd7-4d56c067bc14)

![Скриншот 6](https://github.com/AJDragon01/TOIB_Egorov/assets/145147455/73d58c50-3032-4125-914b-1f7b11cafcd0)

##### 4. Настройка Jupyter Hub

![Скриншот 7](https://github.com/AJDragon01/TOIB_Egorov/assets/145147455/f7f31169-9f59-4e6f-b1e5-c78ccb1697bc)


##### 5. Включение двухфакторной аутентификации OTP
- Включена двухфакторная аутентификация OTP через Keycloak для защищаемого приложения, согласно инструкциям [Ultimate Security](https://ultimatesecurity.pro/post/2fa/) и [MasterTheBoss](https://www.mastertheboss.com/keycloak/how-to-enable-two-factor-authentication-in-keycloak/).

