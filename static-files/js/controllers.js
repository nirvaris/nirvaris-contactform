'use strict';

/* Controllers */

var nirvarisControllers = angular.module('nirvarisApp', []);

nirvarisControllers.controller('nirvarisCtrl', ['$scope', '$http', function($scope, $http) {

}]);

nirvarisControllers.controller('ContactFormCtrl', ['$scope', '$http', function ($scope, $http, $sce) {
	$scope.form;
	
	$scope.sendContactMessage = function(form) {
		// define form
		$scope.form = event.currentTarget;
		
		// set loading button
		$($scope.form).find('button').addClass('btn-loading');
		$($scope.form).find('button').attr('disabled','disabled');
		
		// do ajax
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
			var errors = [];
			var fieldErros;
			var formMessages = response.data.messages;
			
			// reset validations
			$($scope.form).find('.form-error-list').remove();
			$($scope.form).find('div.has-error').removeClass('has-error');
			
			// remove button loading
			$($scope.form).find('button').removeClass('btn-loading');
			$($scope.form).find('button').removeAttr('disabled');
			
			// form messages
			formMessages = response.data.messages;
			if (formMessages) {
				for (var i = 0; i < formMessages.length; i ++) {
					$scope.showFormMessages(formMessages[i].tag, formMessages[i].message);
				}
			}
			
			// field errors
			fieldErros = response.data.form_errors;
			if (fieldErros) {
				angular.forEach(fieldErros, function(value, key) {
				  $scope.showFieldErrorMessage(key, value);
				}, errors);
			}
			
			// clean form fields
			if (response.data.success == 'true') {
				$scope.cleanFormFields();
			}
			
		}, function(response) {
			// called asynchronously if an error occurs
			// or server returns response with an error status.
			console.log("failed :(", response); 
		});
	};
	
	$scope.showFormMessages = function(tag, message){
		var html;
		var messageClassName;
		
		if (tag == 'success') {
			messageClassName = 'alert-success';
		} else if (tag == 'info') {
			messageClassName = 'alert-info';
		} else if (tag == 'warning') {
			messageClassName = 'alert-warning';
		} else if (tag == 'error') {
			messageClassName = 'alert-danger';
		}
		
		html  = '<div class="alert '+ messageClassName +' alert-dismissible" role="alert">';
		html += '<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>';
		html += message
        html += '</div>';
		
		$($scope.form).find('h4').after(html);
	};
	
	$scope.showFieldErrorMessage = function(fieldName, fieldErrors){
		var html;
		
		html = '<ul class="form-error-list">';
		for (var i = 0; i < fieldErrors.length; i ++) {
			html += '<li>' + fieldErrors[i].message + '</li>';
		}
		html += '</ul>';
		
		$($scope.form[ fieldName ]).after( html );
		$($scope.form[ fieldName ]).parent().addClass( 'has-error' );
	};
	
	$scope.cleanFormFields = function() {
		$($scope.form).find('*[name="name"]').val('');
		$($scope.form).find('*[name="email"]').val('');
		$($scope.form).find('*[name="message"]').val('');
	};

}]);