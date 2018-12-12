angular.module('app').service('mqttService', mqttService);

mqttService.$inject = [
    '$rootScope',
];

function mqttService($rootScope) {
    var self = this;

    self.initialize = initialize;
    self.connect = connect;
    self.subscribe = subscribe;
    self.publish = publish;
    self.onConnectionLost = onConnectionLost;
    self.onMessageArrived = onMessageArrived;

    var client = null;

    function initialize(hostname, port, clientId = "clientId") {
        if (!hostname) { throw new Error("Invalid hostname") }
        client = new Paho.MQTT.Client(hostname, Number(port), clientId);
    }

    function connect(callback) {
        if (client == null) { throw new Error("Need to Initialize Mqtt") }
        client.connect({
            onSucess: callback
        });
    }

    function subscribe(topic) {
        if (client == null) { throw new Error("Need to Initialize Mqtt")}
        client.subscribe(topic)
    }

    function publish(message){
        if (client == null) { throw new Error("Need to Initialize Mqtt")}
        var mqtt_message = new Paho.MQTT.Message(message);
        client.send(mqtt_message);
    }

    //called when connection is lost
    function onConnectionLost(callback) {
        if (client == null) { throw new Error("Need to Initialize Mqtt") }
        client.onConnectionLost = callback;
    }

    // called when a message arrives
    function onMessageArrived(callback) {
        if (client == null) { throw new Error("Need to Initialize Mqtt") }
        client.onMessageArrived = callback;
    }

}