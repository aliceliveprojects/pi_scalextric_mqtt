# pi_scalextric_mqtt SPWA
Simple Single Page Web Application (SPWA) testing MQTT.

I suggest not using this SPWA anymore instread I would

- look at the [public brokers list](https://github.com/mqtt/mqtt.github.io/wiki/public_brokers).
- and test using 

*Using ```broker.hivemq.com``` running on port ```8000```(Websockets) works well (must use websocket ports).*

## Broker Details
There are two ways to provide the Mqtt default broker details to the spwa either *Environmental Variables* or *URL Parameters* 


### Environmental Variables

| Variable      | Description  |
| ------------- |:-------------:|
| BROKER_HOST   | Default broker url (OPTIONAL) |
| BROKER_PORT   | Default broker port (OPTIONAL)|

### URL Parameters

example with URL parameters : https://aliceliveprojects.github.io/pi_scalextric_mqtt/spwa/src/index.html#!/index?brokerPort=8000&brokerUrl=broker.hivemq.com

![URL With Broker Details](https://github.com/aliceliveprojects/pi_scalextric_mqtt/blob/master/depreciated_spwa/documentation/url_with_broker_details.png)

example without URL parameters : https://aliceliveprojects.github.io/pi_scalextric_mqtt/spwa/src/index.html#!/index

![URL Without Broker Details](https://github.com/aliceliveprojects/pi_scalextric_mqtt/blob/master/depreciated_spwa/documentation/url_without_broker_details.png)

## Local Deployment

```
npm install
node server.js
```



