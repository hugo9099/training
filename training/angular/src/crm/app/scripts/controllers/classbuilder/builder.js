/**
 * Created by yanspineiro on 5/28/16.
 */
var x =0;
function BuilderCtrl($rootScope,$interval,$interval, $window, $scope, $modal, testtt,Generate) {
    //, $interval, $window, $scope, $modal,  ClassBuilder
    var scope = this;
    $rootScope.template= {};
    scope.fieldList = []
    scope.className = '';
    scope.python_view = false;
    scope.dateDropDownInput = '';
    scope.Test = function(){


        testtt.query(scope.params, function (r) {
            $rootScope.template = r;

        });

    };
    scope.CreateClass = function(){

        scope.params = {'name':scope.className,'fields':scope.fieldList};
        Generate.query(scope.params, function (r) {
            $rootScope.template = r;
            scope.python_view = true;

        });


    };
    scope.Test();


    scope.addField = function(){
        $rootScope.fieldsAtttribute = {}
        UpdateAgentModalInstance = $modal.open(
            {
                templateUrl: 'views/pages/add-fields.html',
                controller: function($modalInstance, $scope){
                    $scope.modalInstance = $modalInstance;
                    return AddFieldCtrl;
                }
            }
        );

        UpdateAgentModalInstance.result.then(function () {
          if ($rootScope.newField != undefined){
              scope.fieldList.push($rootScope.newField);
          };

        });
    };


    scope.update = function(field){

        $rootScope.newField = field;
        UpdateAgentModalInstance = $modal.open(
            {
                templateUrl: 'views/pages/add-fields.html',
                controller: function($modalInstance, $scope){
                    $scope.modalInstance = $modalInstance;
                    return AddFieldCtrl;
                }
            }
        );

        UpdateAgentModalInstance.result.then(function () {
            if ($rootScope.newField != undefined){
                field = $rootScope.newField;
            };

        });
    };

}
angular
    .module('sbAdminApp')
    .controller('BuilderCtrl', BuilderCtrl);
