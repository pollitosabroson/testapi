app.config([
    '$contentProvider', '$stateProvider',
    function($contentProvider, $stateProvider) {
        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: $contentProvider.url('base.html'),
                controller: 'HomeCtrl'
            })
            .state('create', {
                url: '/createuser',
                templateUrl: $contentProvider.url('createusers.html'),
            })

    }
]);
