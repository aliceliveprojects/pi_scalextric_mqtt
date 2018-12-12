angular.module('app').controller('IndexViewCtrl', IndexViewCtrl);

IndexViewCtrl.$inject = [
    '$rootScope',
    'mqttService'
];

function IndexViewCtrl($rootScope, mqttService) {
    var vm = this;

    vm.ip_address = $rootScope.defaultUrl;
    vm.mqtt_topic = "";
    vm.mqtt_message = "";
    vm.logs = "hi"
    vm.subscribe = subscribe;
    vm.publish = publish;

    function subscribe(valid) {
        if (!valid) {
            alert("Invalid Details")
        } else {
            mqttService.subscribe(vm.mqtt_topic);
        }
    }

    function publish(valid) {
        if (!valid || !vm.mqtt_message) {
            alert("Invalid Details")
        } else {
            mqttService.publish(vm.mqtt_topic,vm.mqtt_message);
        }
    }

    activate();
    function activate() {
        console.log("connecting to mqtt");
        //connection only works with broker.hivemq.com
        //taken from https://github.com/mqtt/mqtt.github.io/wiki/public_brokers
        mqttService.initialize("broker.hivemq.com", 8000);
        mqttService.onConnectionLost(function () {
            console.error("connection lost");
        });
        mqttService.onMessageArrived(function (message) {
            console.log("message arrived ", message);
            vm.logs += (message.payloadString);
        });
        mqttService.connect(function () {
            console.log("connected");
        });
    }
}