# pi_scalextric_mqtt
Simple application testing MQTT using a Node-Red and a Single Page Web Application (SPWA)

## Local Deployment
The SPWA is served up by the Raspberry Pi, however can be used locally.

Before deploying the default url and port need to be changed located in app.js

I recommend looking at the [public_brokers list](https://github.com/mqtt/mqtt.github.io/wiki/public_brokers).

Using ```broker.hivemq.com``` running on port ```8000```(Websockets) works well (must use websocket ports).

**Install packages ```npm install```**

**To run ```node server.js```**

