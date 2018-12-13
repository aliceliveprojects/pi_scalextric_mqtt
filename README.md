# pi_scalextric_mqtt
Simple application testing MQTT using a Node-Red and a Single Page Web Application (SPWA)

## Setting Http Server
Setting up Raspberry Pi to serve a SPWA

### Static IP

*Setting a static ip will disconnect the Pi from the interent please read the Http Server section and install the needed modules*

Once the Pi is connected to the router, a static ip needs to be configured. 

The Pi ip address should be : ```192.168.1.3```

The Pi routers address should be : ```192.168.1.1```

To configure a static ip either follow the intructions below or from [Raspberry Pi Org](https://www.raspberrypi.org/learning/networking-lessons/rpi-static-ip-address/) or [Raspberry Pi Org Archived](http://web.archive.org/web/20181213192602/https://www.raspberrypi.org/learning/networking-lessons/rpi-static-ip-address/)

Open a terminal and type ```sudo nano /etc/dhcpcd.conf``` and append this to the bottom of the script

```
interface eth0

static ip_address=192.168.1.3/24
static routers=192.168.1.1
static domain_name_servers=192.168.0.1

interface wlan0

static ip_address=192.168.1.3/24
static routers=192.168.1.1
static domain_name_servers=192.168.0.1
```

### Http Server
Once a static ip has been configured, a http server can be deployed.

Before we begin, if not already you will need nodejs and npm. To install simply run ```sudo apt-get install nodejs npm```

Once nodejs and npm are installed we will need the http-server package. To install run ```sudo npm install http-server -g```,

To start the server run ```http-server --cors```

