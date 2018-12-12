angular.module('app').controller('IndexViewCtrl', IndexViewCtrl);

IndexViewCtrl.$inject = [
    '$rootScope',
    'mqttService'
];

function IndexViewCtrl($rootScope,mqttService) {
    var vm = this;

    vm.ip_address = $rootScope.defaultUrl;
    vm.mqtt_topic = "";
    vm.mqtt_message = "";
    vm.go = go;

    function go(valid) {
        if (!valid) {
            alert("Invalid Details")
        } else {
           console.log("valid");
          
            
        }

    }

    activate();


    function activate(){
        mqttService.initialize("t","1");
    }
}