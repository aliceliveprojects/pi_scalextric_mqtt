angular.module('app').controller('IndexViewCtrl', IndexViewCtrl);

IndexViewCtrl.$inject = [
    '$rootScope',
];

function IndexViewCtrl($rootScope) {
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
}