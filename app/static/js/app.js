var app = angular.module('app', []);
function Ctrl($scope, $http) {
	$scope.search = function() {
		$http.get('/places/search/', {q:$scope.query})
			.success(function(data, status, headers, config) {
				$scope.places = data;
			})
	};
}
