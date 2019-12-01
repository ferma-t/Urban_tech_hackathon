var app = angular.module('service', []);

app.factory('GetUser', function ($resource) {
    return $resource("/api/user/:pk/?format=json",{
        pk: "@pk"
      });
});

app.factory('Processes', function ($resource) {
    return $resource("/api/processes/?format=json");
});

app.factory('Tasks', function ($resource) {
    return $resource("/api/???/?format=json");
});