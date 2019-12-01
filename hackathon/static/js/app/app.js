var app = angular.module('app', [
    'ngResource',    
    'service', 
    'main-ctrl',
    'ui.tree',
]);

app.config([
    "$interpolateProvider",
    "$locationProvider",
    "$httpProvider",
    function($interpolateProvider, $locationProvider, $httpProvider) {
        $interpolateProvider.startSymbol("[[");
        $interpolateProvider.endSymbol("]]");

        $locationProvider.html5Mode({
            enabled: true,
            requireBase: false,
            rewriteLinks: false
        });

        $httpProvider.defaults.headers.post["X-Requested-With"] =
            "XMLHttpRequest";
        $httpProvider.defaults.xsrfCookieName = "csrftoken";
        $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
    }
]);