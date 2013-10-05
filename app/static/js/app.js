var app = angular.module('app', []);
function Ctrl($scope, $http) {
	angular.extend($scope, {
		center: {
			latitude: 0,
			longitude: 0
		},
		markers: [],
		zoom: 8
	});
	$scope.search = function() {
		$http.get('/places/search/', {q:$scope.query})
			.success(function(data, status, headers, config) {
				$scope.places = data;
				$scope.markers = [];
				for(var place in data) {
					$scope.markers.push({latitude:place.lat, longitude:place.lng});
				}
			})
	};
}
