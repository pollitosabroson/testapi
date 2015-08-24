app.directive('users', [ 'getUsers', function (getUsers) {
  return {
    restrict: 'E',
    controller: function($scope, $element, $attrs){
      $scope.users = getUsers.query();
    },
    templateUrl:  '/assets/templates/users.html'
  };
}
]);

app.directive('creatuser', [ 'getUsers', function ( getUsers) {
  return {
   replace: true,
   template: '<form novalidate role="form" name="loginForm" ng-submit="submitForm(credenciales)">'+
            '<fieldset>'+
              '<div class="form-group">'+
                '<input type="text" class="form-control" placeholder="Primer nombre" name="nombre" required="required" autofocus="autofocus" ng-model="credenciales.nombre">'+
              '</div>'+
               '<div class="form-group">'+
                '<input type="text" class="form-control" placeholder="Apellidos" name="apellidos" required="required" autofocus="autofocus" ng-model="credenciales.apellidos">'+
              '</div>'+
              '<div class="form-group">'+
                '<input type="email" class="form-control" placeholder="Correo electŕonico" name="email" required="required" autofocus="autofocus" ng-model="credenciales.email">'+
              '</div>'+
              '<div class="form-group">'+
                '<input type="date" class="form-control" placeholder="Cumpleaños" name="cumpleaños" required="required" autofocus="autofocus" ng-model="credenciales.cumpleanos">'+
              '</div>'+
              '<div class="form-group">'+
                '<input type="password" class="form-control" placeholder="Contraseña" name="password" required="required" autofocus="autofocus" ng-model="credenciales.password">'+
              '</div>'+
              '<input type="submit" class="btn btn-primary btn-block" value="Iniciar sesión" ng-disabled="loginForm.$invalid"/>'+
            '</fieldset>'+
        '</form>',
    controller: function ($scope, $filter) {
        $scope.submitForm = function (data) {
            data.cumpleanos = $filter('date')(data.cumpleanos, 'yyyy-MM-dd', '')
            console.log(data)
            var user = new getUsers(
                data
            )
            user.$save(function (data) {
                console.log(data)
            })
        }
    }
  };
}
]);