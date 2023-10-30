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

![Скриншот 2](https://drive.google.com/file/d/1qCV0jAp_D39E7U3DPOkOfmKI8fAmZMiV/view?usp=share_link)

![Скриншот 3](https://drive.google.com/file/d/1NRJK_UZ7bteQmPKqJucDOmVv9S8lbtIj/view?usp=sharing)

![Скриншот 4](https://drive.google.com/file/d/1Yl2LiCMlg2J2oZ3sZWe7ez9luSCVFB1G/view?usp=sharing)


##### 5. Включение двухфакторной аутентификации OTP
- Включена двухфакторная аутентификация OTP через Keycloak для защищаемого приложения, согласно инструкциям [Ultimate Security](https://ultimatesecurity.pro/post/2fa/) и [MasterTheBoss](https://www.mastertheboss.com/keycloak/how-to-enable-two-factor-authentication-in-keycloak/).

