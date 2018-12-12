angular.module('app').service('dataService', dataService);

dataService.$inject = [
    '$rootScope',
    '$http'
];

function dataService($rootScope, $http) {
    var self = this;


    self.publishMessage;


    /*
        Sends post request to publish mqtt message

        Path : /topic/:topicName/:message
        Method : Post
    */
    function publishMessage(ip_address,topic,message) {


        if (!ip_address) { ip_address = $rootScope.defaultUrl; }

        var url = 'http://' + ip_address + '/topic/' + topic + '/' + message;

        return $http.post(url);
    }

   

}