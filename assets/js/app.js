'use strict';

var app = angular.module('app', [
    'ngResource', 'ui.router', 'vo.api', 'vo.content'
]);

app.config([
    '$apiProvider', '$contentProvider', '$httpProvider', '$locationProvider',
    function($apiProvider, $contentProvider, $httpProvider, $locationProvider) {
        /* Configure api endpoint */
        $apiProvider.apiEndpoint = 'http://' + window.location.host + '/api';
        $apiProvider.apiUsesTrailingSlash = false;

        /* Configure content base url */
        $contentProvider.urlPrefix = '/assets/templates/';

        /* Enable HTML5 mode */
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');      

    }
]);

app.run([
    '$rootScope', '$content',
    function($rootScope, $content) {
        // Check route permissions and start the progress bar if required.
        $rootScope.$content = $content;

    }
]);