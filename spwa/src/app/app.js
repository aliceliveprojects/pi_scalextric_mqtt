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
        url: '/index',
        templateUrl: 'app/shared/index/indexView.html',
        controller: 'IndexViewCtrl',
        controllerAs: 'indexView'
    }

  
    $stateProvider.state(indexState);


    $urlRouterProvider.otherwise('/index');

  
}

angular.module('app').run(run);

run.$inject = [
    '$rootScope'
]

function run($rootScope) {
    console.log('version 1.0.0');
    $rootScope.defaultUrl = '192.168.1.102';
    $rootScope.defaultPort = '9001';
}
