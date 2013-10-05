function app($scope) {
	$scope.search = function() {
		$http.get('/places/search', {q:$scope.query})
			.success(function(data, status, headers, config) {
			
			})
	};
}