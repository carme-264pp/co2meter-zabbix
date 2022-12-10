# CO2 Meter read and send to zabbix

This scripts supports Python 3.x.

## Setup

### Install Python modules

1. Install CO2Meter Python module

    Install CO2Meter with pip:
    ```bash
    $ sudo pip install git+https://github.com/heinemml/CO2Meter
    ```

1. Install PyZabbix

    Install PyZabbix with pip:
    ```bash
    $ sudo pip install pyzabbix
    ```
### Zabbix watching

1. write crontab

    ```bash
    $ sudo crontab -e

    # every 1 minute
    */1 * * * * /usr/bin/python3 /opt/co2meter/co2-zabbix.py >> /opt/co2meter/co2-zabbix.log
    ```

1. Import zabbix template

   Import co2meter-zabbix-template.yaml to your zabbix server.

## Simple use

```bash
sudo python3 co2-terminal.py
```
