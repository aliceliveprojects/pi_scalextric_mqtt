# pi_scalextric_mqtt SPWA
Simple Single Page Web Application (SPWA) testing MQTT, [check it out](https://aliceliveprojects.github.io/pi_scalextric_mqtt/spwa/src/index.html#!/index)

I recommend looking at the [public brokers list](https://github.com/mqtt/mqtt.github.io/wiki/public_brokers).

*Using ```broker.hivemq.com``` running on port ```8000```(Websockets) works well (must use websocket ports).*

## Local Deployment

| Variable      | Description  |
| ------------- |:-------------:|
| BROKER_HOST   | Default broker url (OPTIONAL) |
| BROKER_PORT   | Default broker port (OPTIONAL)|


```
npm install
BROKER_HOST='192.168.1.3' BROKER_PORT='9001' node server.js
```



