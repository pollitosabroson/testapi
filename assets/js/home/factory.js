app.factory('getUsers', ['$resource', '$api',
    function($resource, $api) {
        return $resource($api.url('/users'));
    }
]);