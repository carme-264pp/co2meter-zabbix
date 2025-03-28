# CO2 Meter read and send to zabbix

This scripts supports Python 3.x.

## Setup

### Install Python modules

1. Create venv

    Install CO2Meter with pip:
    ```shell
    $ python3 -m venv lib
    $ source ./lib/bin/activate
    ```

1. Install Python library

    ```shell
    $ pip3 install -r requirements.txt
    ```
### Install CO2-Zabbix 

1. Install Systemd unit files

    ```shell
    $ sudo cp co2-zabbix.service co2-zabbix.timer /etc/systemd/system/
    $ sudo systemctl daemon-reload
    $ sudo systemctl enable co2-zabbix.timer
    $ sudo systemctl start co2-zabbix.timer
    ```

    Verify
    ```shell
    $ systemctl list-timers
    ```

1. Import zabbix template

   Import co2meter-zabbix-template.yaml to your zabbix server.

## Simple use

```shell
sudo python3 co2-terminal.py
```
