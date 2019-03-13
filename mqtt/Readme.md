# pi_scalextric_mqtt

## Src Folder Project Structure
 - [Config](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt/src/Config): example config files and documentation
 - [QrCode](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt/src/QrCode): qr-generation code and documentation
 - [Scripts/SensorScripts](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt/src/Scripts/sensorScripts): sensors scripts and documentation


---


## Setting Up MQTT 

### Local Broker Using Mosquitoo

*When communicating via mqtt from client side Javascript MQTT over Websockets is recommended. For Javascript there is both a pure MQTT library and the Paho in page library that uses websockets*

#### Without Websockets
The Mosquitto Broker 1.4 comes with Raspbian Stretch. If Raspbian Jesse is being used Mosquitto can be built from source, follow this tutorial [StackExchange](https://raspberrypi.stackexchange.com/questions/80051/how-to-upgrade-mosquitto-mqtt-to-the-latest-version) or [StackExchange Archived](http://web.archive.org/web/20181213135759/https://raspberrypi.stackexchange.com/questions/80051/how-to-upgrade-mosquitto-mqtt-to-the-latest-version)

#### With Websockets
By default Mosquitto Broker 1.4 it not configured with websockets. Follow this tutorial to configure Mosquitto with websockets
[Mosquitto Websocket](https://gist.github.com/smoofit/dafa493aec8d41ea057370dbfde3f3fc) or [Mosquitto Websocket Archived](http://web.archive.org/web/20181213140654/https://gist.github.com/smoofit/dafa493aec8d41ea057370dbfde3f3fc)

*The broker starts automatically on boot, to stop the broker sudo /etc/init.d/mosquitto stop & to re-start sudo /etc/init.d/mosquitto start* 

---

### Cloud Broker Using Heroku & CloudMQTT

*CloudMQTT free tier is extremely restrictive only allowing upto and 5 connections, only use this for testing*

*A verified Heroku account is needed & Heroku Box region must be the United States*



To setup a Mqtt Broker on Heroku first create a new application. Within the application panel navigate to the Resources tab. Within the resources tab under the Add-ons section search for CloudMQTT installing the free tier.
Once CloudMQTT is installed click on the add-on to view broker details. 

### Public Broker

There are many public brokers around. They tend to be a blit flaky and break often, but even when located on th other side of the planet, their performance is good. Latency is very low indeed.
If you're planning on using GitHub to host your SPWA, then your broker must support WSS (secure web sockets). You can't use WS(unsecured) SPWA will be served over HTTPS, and shifting to WS represents a security risk and will be blocked by your browser.

We have found https://test.mosquitto.org/ to be the most reliable public service.


## Node Red

Node-Red flow that publishes and subscribes to a single topic

### Node-Red Flow

To import a Node-Red flow simple navigate ```Menu > Import > Clipboard``` and copy and paste the flow below

```

[{"id":"49b63d55.4ba564","type":"tab","label":"Example Mqtt ","disabled":false,"info":"Example mqtt subscribe and publish flow"},{"id":"91abdb37.974d18","type":"inject","z":"49b63d55.4ba564","name":"","topic":"","payload":"Hi there","payloadType":"str","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":130,"y":120,"wires":[["b00c673f.95bed8"]]},{"id":"a00b3493.851bb8","type":"mqtt in","z":"49b63d55.4ba564","name":"Subscribe to Example Topic","topic":"Example","qos":"2","broker":"34498743.f24228","x":500,"y":120,"wires":[["f2834f34.b2639"]]},{"id":"b00c673f.95bed8","type":"mqtt out","z":"49b63d55.4ba564","name":"Publish to Example Topic","topic":"Example","qos":"","retain":"","broker":"34498743.f24228","x":190,"y":160,"wires":[]},{"id":"f2834f34.b2639","type":"debug","z":"49b63d55.4ba564","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","x":450,"y":180,"wires":[]},{"id":"eb8a57c.e5323a8","type":"comment","z":"49b63d55.4ba564","name":"Publish Message to Topic","info":"","x":190,"y":80,"wires":[]},{"id":"9e66e1e.727a72","type":"comment","z":"49b63d55.4ba564","name":"Subscribe to Topic","info":"","x":470,"y":80,"wires":[]},{"id":"34498743.f24228","type":"mqtt-broker","z":"","name":"","broker":"localhost","port":"1883","clientid":"","usetls":false,"compatmode":true,"keepalive":"60","cleansession":true,"birthTopic":"","birthQos":"0","birthPayload":"","closeTopic":"","closeQos":"0","closePayload":"","willTopic":"","willQos":"0","willPayload":""}]

```

---


This is the work of [Yusof Bandar](https://github.com/YusofBandar) for [DigitalLabs@MMU](https://digitallabs.mmu.ac.uk/).

<p align="center">
<img align="middle" src="https://trello-attachments.s3.amazonaws.com/5b2caa657bcf194b4d089d48/5b98c7ec64145155e09b5083/d2e189709d3b79aa1222ef6e9b1f3735/DigitalLabsLogo_512x512.png"  />
 </p>
 
 
<p align="center">
<img align="middle" src="https://trello-attachments.s3.amazonaws.com/5b2caa657bcf194b4d089d48/5b98c7ec64145155e09b5083/e5f47675f420face27488d4e5330a48c/logo_mmu.png" />
 </p>

