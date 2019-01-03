angular.module('app').service('mqttService', mqttService);

mqttService.$inject = [
];


/*
    Mqtt Service uses Eclipse Paho JavaScript Client found :
        - https://github.com/eclipse/paho.mqtt.javascript
        - https://web.archive.org/web/20181212171208/https://github.com/eclipse/paho.mqtt.javascript
*/
function mqttService() {
    var self = this;

    self.initialize = initialize;
    self.connect = connect;
    self.subscribe = subscribe;
    self.publish = publish;
    self.onConnectionLost = onConnectionLost;
    self.onMessageArrived = onMessageArrived;

    var client = null;

    // Initialize mqtt client, this must be the done before any other actions
    function initialize(hostname, port, clientId = "clientId") {
        if (!hostname) { throw new Error("Invalid hostname") }
        if (!port) { throw new Error("Invalid port")}
        client = new Paho.MQTT.Client(hostname, Number(port), clientId);
    }

    //connect to the mqtt broker
    function connect(callback,username,password,ssl=false) {
        if (!client) { throw new Error("Need to Initialize Mqtt") }

        var mqttOptions = {
            onSuccess : callback,
            onFailure : function(error){
                console.log(error);
            },
            useSSL : ssl
        }

        if(username) mqttOptions.userName = username;
        if(password) mqttOptions.password = password;
        
        client.connect(mqttOptions);
    }

    //subscribe to a mqtt topic, when message arrives client.onMessageArrived is called
    function subscribe(topic) {
        if (!client) { throw new Error("Need to Initialize Mqtt")}
        client.subscribe(topic)
    }

    //publish mqtt message
    function publish(topic,message){
        if (!client) { throw new Error("Need to Initialize Mqtt")}
        var mqtt_message = new Paho.MQTT.Message(message);
        mqtt_message.destinationName = topic;
        client.send(mqtt_message);
    }

    //called when connection is lost
    function onConnectionLost(callback) {
        if (!client) { throw new Error("Need to Initialize Mqtt") }
        client.onConnectionLost = callback;
    }

    // called when a message arrives
    function onMessageArrived(callback) {
        if (!client) { throw new Error("Need to Initialize Mqtt") }
        client.onMessageArrived = callback;
    }

}
