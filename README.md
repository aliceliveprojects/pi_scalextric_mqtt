# pi_scalextric_mqtt
Simple application testing MQTT using a Node-Red and a Single Page Web Application (SPWA)

## Setting Mosquitto Broker

* If a a client needs to communicate vai mqtt, Mosquitto Broker needs to be configured using webscocket. Client side mqtt using websockets insetad of mqtt 

### Without Websockets
The Mosquitto Broker 1.4 comes with Raspbian Stretch. If Raspbian Jesse is being used Mosquitto can be built from source, follow this tutorial [StackExchange](https://raspberrypi.stackexchange.com/questions/80051/how-to-upgrade-mosquitto-mqtt-to-the-latest-version) or [StackExchange Archived](http://web.archive.org/web/20181213135759/https://raspberrypi.stackexchange.com/questions/80051/how-to-upgrade-mosquitto-mqtt-to-the-latest-version)

### With Websockets
By default Mosquitto Broker 1.4 it not configured with websockets. Follow this tutorial to configure Mosquitto with websockets
[Mosquitto Websocket](https://gist.github.com/smoofit/dafa493aec8d41ea057370dbfde3f3fc) or [Mosquitto Websocket Archived](http://web.archive.org/web/20181213140654/https://gist.github.com/smoofit/dafa493aec8d41ea057370dbfde3f3fc)



