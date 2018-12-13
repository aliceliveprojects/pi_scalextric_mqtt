# pi_scalextric_mqtt
Simple application testing MQTT using a Node-Red and a Single Page Web Application (SPWA)

- [Mqtt](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt)
- [SPWA](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/spwa/src)

## Setting Http Server
Setting up Raspberry Pi to serve a SPWA

### Static IP

*Setting a static ip will disconnect the Pi from the interent please read the Http Server section and install the needed modules*

Once the Pi is connected to the router, a static ip needs to be configured. 

**The Pi ip address should be : ```192.168.1.3```**

**The Pi routers address should be : ```192.168.1.1```**

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

*If another ip address is being used, the default ip address needs to be changed within the SPWA located in app.js*

---

### Http Server
Once a static ip has been configured, a http server can be deployed.

**Install nodejs and npm ```sudo apt-get install nodejs npm```**

Once nodejs and npm are installed we will need the http-server package. 

**Install http-server ```sudo npm install http-server -g```**

Start the server ```http-server --cors```

*To run on https read https://digitallabs.mmu.ac.uk/taming-the-urban-wild/#more-1657*

