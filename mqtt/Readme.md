# pi_scalextric_mqtt
Setting up Mqtt on a Raspberry Pi using Mosquitto

## Setting Mosquitto Broker

*When communicating via mqtt from client side Javascript MQTT over Websockets is recommended. For Javascript there is both a pure MQTT library and the Paho in page library that uses websockets*

### Without Websockets
The Mosquitto Broker 1.4 comes with Raspbian Stretch. If Raspbian Jesse is being used Mosquitto can be built from source, follow this tutorial [StackExchange](https://raspberrypi.stackexchange.com/questions/80051/how-to-upgrade-mosquitto-mqtt-to-the-latest-version) or [StackExchange Archived](http://web.archive.org/web/20181213135759/https://raspberrypi.stackexchange.com/questions/80051/how-to-upgrade-mosquitto-mqtt-to-the-latest-version)

### With Websockets
By default Mosquitto Broker 1.4 it not configured with websockets. Follow this tutorial to configure Mosquitto with websockets
[Mosquitto Websocket](https://gist.github.com/smoofit/dafa493aec8d41ea057370dbfde3f3fc) or [Mosquitto Websocket Archived](http://web.archive.org/web/20181213140654/https://gist.github.com/smoofit/dafa493aec8d41ea057370dbfde3f3fc)



## Node Red

Node-Red flow that publishes and subscribes to a single topic

### Node-Red Flow

To import a Node-Red flow simple navigate ```Menu > Import > Clipboard``` and copy and paste the flow below

```

[{"id":"49b63d55.4ba564","type":"tab","label":"Example Mqtt ","disabled":false,"info":"Example mqtt subscribe and publish flow"},{"id":"91abdb37.974d18","type":"inject","z":"49b63d55.4ba564","name":"","topic":"","payload":"Hi there","payloadType":"str","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":130,"y":120,"wires":[["b00c673f.95bed8"]]},{"id":"a00b3493.851bb8","type":"mqtt in","z":"49b63d55.4ba564","name":"Subscribe to Example Topic","topic":"Example","qos":"2","broker":"34498743.f24228","x":500,"y":120,"wires":[["f2834f34.b2639"]]},{"id":"b00c673f.95bed8","type":"mqtt out","z":"49b63d55.4ba564","name":"Publish to Example Topic","topic":"Example","qos":"","retain":"","broker":"34498743.f24228","x":190,"y":160,"wires":[]},{"id":"f2834f34.b2639","type":"debug","z":"49b63d55.4ba564","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","x":450,"y":180,"wires":[]},{"id":"eb8a57c.e5323a8","type":"comment","z":"49b63d55.4ba564","name":"Publish Message to Topic","info":"","x":190,"y":80,"wires":[]},{"id":"9e66e1e.727a72","type":"comment","z":"49b63d55.4ba564","name":"Subscribe to Topic","info":"","x":470,"y":80,"wires":[]},{"id":"34498743.f24228","type":"mqtt-broker","z":"","name":"","broker":"localhost","port":"1883","clientid":"","usetls":false,"compatmode":true,"keepalive":"60","cleansession":true,"birthTopic":"","birthQos":"0","birthPayload":"","closeTopic":"","closeQos":"0","closePayload":"","willTopic":"","willQos":"0","willPayload":""}]

```

