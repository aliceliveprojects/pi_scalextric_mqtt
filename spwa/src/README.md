# pi_scalextric_mqtt SPWA
Simple Single Page Web Application (SPWA) testing MQTT.

I recommend looking at the [public brokers list](https://github.com/mqtt/mqtt.github.io/wiki/public_brokers).

*Using ```broker.hivemq.com``` running on port ```8000```(Websockets) works well (must use websocket ports).*

## Broker Details
There are two ways to provide the Mqtt default broker details to the spwa either *Environmental Variables* or *URL Parameters* 


### Environmental Variables

| Variable      | Description  |
| ------------- |:-------------:|
| BROKER_HOST   | Default broker url (OPTIONAL) |
| BROKER_PORT   | Default broker port (OPTIONAL)|

### URL Parameters

example with URL parameters : https://aliceliveprojects.github.io/pi_scalextric_mqtt/spwa/src/index.html#!/index?brokerPort=9001&brokerUrl=192.168.1.3

example without URL parameters : https://aliceliveprojects.github.io/pi_scalextric_mqtt/spwa/src/index.html#!/index

## Local Deployment

```
npm install
node server.js
```



