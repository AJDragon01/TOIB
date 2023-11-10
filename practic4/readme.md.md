# Настройка Rsyslog для сбора логов

## Подготовка виртуальных машин

1. **Создание виртуальных машин на базе Debian 12**

    Установите виртуальные машины на базе ОС Debian 12, используя [VirtualBox](https://www.virtualbox.org/wiki/Downloads) и [Debian 12.1.0 netinst ISO](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.1.0-amd64-netinst.iso).

2. **Настройка сетевого обмена между виртуальными машинами**

    Следуйте [руководству VirtualBox](https://www.virtualbox.org/manual/ch06.html), чтобы обеспечить сетевой обмен между созданными виртуальными машинами.

### Настройка Rsyslog на сервере и клиенте

3. **Передача логов с 1-й ВМ на 2-ю ВМ с использованием rsyslog**

    Перейдите по [этой инструкции](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/) для включения передачи логов с 1-й ВМ на 2-ю ВМ с помощью Rsyslog.



## Настройка Rsyslog на сервере

1. **Установка Rsyslog**

 

    Для Debian / Ubuntu:

    ```bash
    apt-get install rsyslog
    ```
![Alt text](<Снимок экрана 2023-11-03 в 12.45.38.png>)
2. **Настройка Rsyslog сервера**

    Откройте конфигурационный файл Rsyslog:

    ```bash
    vi /etc/rsyslog.conf
    ```

    Раскомментируйте строки для включения прослушивания по UDP и TCP на порту 514:

    ```bash
    $ModLoad imudp
    $UDPServerRun 514

    $ModLoad imtcp
    $InputTCPServerRun 514
    ```

    Добавьте следующие строки для создания шаблона логов и отправки их в определенное место:

    ```bash
    $template RemoteLogs,"/var/log/rsyslog/%HOSTNAME%/%PROGRAMNAME%.log"
    *.* ?RemoteLogs
    & ~
    ```

    Перезапустите службу Rsyslog для применения изменений:

    ```bash
    systemctl restart rsyslog
    ```
![Alt text](<Снимок экрана 2023-11-09 в 11.26.27.png>)
## Настройка Rsyslog на клиенте

1. **Установка и запуск Rsyslog**

    Установите Rsyslog на клиенте и запустите его.

2. **Отправка всех логов на сервер**

    Создайте новый файл конфигурации для Rsyslog:

    ```bash
    vi /etc/rsyslog.d/all.conf
    ```

    Добавьте следующую строку, чтобы отправить все логи на сервер:

    ```bash
    *.* @@192.168.1.4:514
    ```

    > Здесь `192.168.1.4` - IP-адрес вашего сервера для логов.

    Перезапустите службу Rsyslog на клиенте.
![Alt text](<Снимок экрана 2023-11-09 в 11.27.01.png>)
Эти шаги помогут настроить Rsyslog на сервере для приема логов и на клиенте для отправки всех логов на сервер. После успешной настройки, логи будут поступать на сервер для дальнейшего анализа и обработки.
![Alt text](<Снимок экрана 2023-11-09 в 11.27.41.png>)
![Alt text](<Снимок экрана 2023-11-09 в 11.25.48.png>)

## Настройка сбора логов с помощью Loki

### Запустите Docker Compose
```bash
docker-compose up -d
```
![Alt text](<Снимок экрана 2023-11-10 в 10.57.47.png>)

### Запуск Grafana
1. ***Откройте Grafana в вашем браузере по адресу http://localhost:3000 .*** 


2. ***Настра панель управления Loki в Grafana сиваем панель использованием источника данных Loki и выводим логи .***
![Alt text](<Снимок экрана 2023-11-10 в 13.15.48.png>)

## Установка и настройка Signoz

### 1. Установка Signoz

```bash
# Клонировать репозиторий с Docker Compose файлом
git clone https://github.com/Signoz/signoz.git

# Перейти в каталог с Docker Compose файлом
cd signoz/deploy

# Запустить Signoz 
./install.sh
```
![Alt text](<Снимок экрана 2023-11-10 в 14.31.26.png>)
### 2. Создание учетной записи
![Alt text](<Снимок экрана 2023-11-10 в 14.36.35.png>)

### 3. Проверка 
![Alt text](<Снимок экрана 2023-11-10 в 14.37.46.png>)

## В начало 
[Тык](https://github.com/AJDragon01/TOIB_Egorov)