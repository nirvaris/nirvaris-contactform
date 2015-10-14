'use strict';

/* Controllers */

var nirvarisControllers = angular.module('nirvarisApp', []);

nirvarisControllers.controller('nirvarisCtrl', ['$scope', '$http', function($scope, $http) {

}]);


nirvarisControllers.controller('ContactFormCtrl', ['$scope', '$http', function ($scope, $http, $sce) {
	$scope.sendContactMessage = function(form) {
		$http.post('#', $.param({ 
			name: angular.element(document.getElementsByName('name')[0]).val(),
			email: angular.element(document.getElementsByName('email')[0]).val(),
			message: angular.element(document.getElementsByName('message')[0]).val(),
			send_to_me: document.getElementsByName('send_to_me')[0].checked,
			anti_spam_token: angular.element(document.getElementsByName('anti_spam_token')[0]).val(),
			anti_spam_hidden: angular.element(document.getElementsByName('anti_spam_hidden')[0]).val(),
			csrfmiddlewaretoken: angular.element(document.getElementsByName('csrfmiddlewaretoken')[0]).val() 
		}), {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}).
		then(function(response) {
			// this callback will be called asynchronously
			// when the response is available
			$scope.words = response.data; 
		}, function(response) {
			// called asynchronously if an error occurs
			// or server returns response with an error status.
			console.log("failed :(", response); 
		});
	};

}]);