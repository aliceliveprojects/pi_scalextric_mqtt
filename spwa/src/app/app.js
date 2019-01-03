angular.module('app', ['ui.router']);


angular.module('app').config(config);

config.$inject = [
    '$stateProvider',
    '$urlRouterProvider'
]

function config($stateProvider, $urlRouterProvider) {

    /* 
     Index Page
     user can enter ip address and channel number
    */
    var indexState = {
        name: 'index',
        url: '/index?brokerUrl&brokerPort',
        params: {
            brokerUrl: {
                dynamic: false
            },
            brokerPort: {
                dynamic: false
            }
        },
        templateUrl: 'app/shared/index/indexView.html',
        controller: 'IndexViewCtrl',
        controllerAs: 'indexView',
        resolve: {
            broker: ['$stateParams','brokerDetails', function ($stateParams,brokerDetails) {
                if($stateParams.brokerUrl) brokerDetails.HOST = $stateParams.brokerUrl;
                if($stateParams.brokerPort) brokerDetails.PORT = $stateParams.brokerPort;
            }]
        }
    }


    $stateProvider.state(indexState);

    $urlRouterProvider.otherwise('/index');
}

angular.module('app').run(run);

run.$inject = [
    '$rootScope'
]

function run() {
    console.log('version 1.0.0 Yusof Bandar');
}
