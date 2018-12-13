angular.module('app').controller('IndexViewCtrl', IndexViewCtrl);

IndexViewCtrl.$inject = [
    '$rootScope',
    '$scope',
    'mqttService'
];

function IndexViewCtrl($rootScope, $scope, mqttService) {
    var vm = this;
    var count = 0;

    vm.ip_address = $rootScope.defaultUrl;
    vm.port = $rootScope.defaultPort;
    vm.mqtt_topic = "";
    vm.mqtt_message = "";
    vm.logs = ""
    vm.subscribe = subscribe;
    vm.publish = publish;
    vm.connect = connect;
    vm.clear = clear;

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
            mqttService.publish(vm.mqtt_topic, vm.mqtt_message);
        }
    }

    function clear() {
        vm.logs = "";
    }

    function connect() {
        console.log("connecting to mqtt");

        mqttService.initialize(vm.ip_address,vm.port);
        mqttService.onConnectionLost(function () {
            console.error("connection lost");
        });
        mqttService.onMessageArrived(function (message) {
            console.log("message arrived ", message);
            count += 1;
            vm.logs += count + ") Message Arrived : " + (message.payloadString) + "   ";
            $scope.$apply(function () {

            });
        });
        mqttService.connect(function () {
            console.log("connected");
        });
    }


}