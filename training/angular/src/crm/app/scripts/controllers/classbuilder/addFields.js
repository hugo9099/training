/**
 * Created by yanspineiro on 7/3/16.
 */
function AddFieldCtrl($rootScope, $interval, $interval, $window, $scope, $modal, testtt) {
    //, $interval, $window, $scope, $modal,  ClassBuilder
    var scope = this;
    scope.have_admin = false;
    scope.have_serializer = false;

    scope.fieldAttribute = {
        'name': '',
        'dataType': '',
        'default': '',
        'allowBlank': false,
        'allowNull': true,
        'auto_now_add': false,
        'max_length': '',
        'verbose_name': '',
        'ForeignKey': '',
        'primary_key': false,
        'display': true,
        'admin': {},
        'serializer': {}
    };
    scope.admin = {
        'isdisplayname': false,
        'is_searchfield': false,
        'is_filter': false,
        'is_readOnly': false
    };
    scope.serializer = {
        'allow_blank': true,
        'default': '',
        'source': '',
        'required': false
    };


    scope.typeChoice = [{label:'TEXT', id: 'CharField'},
        {label:'DateTime', id: 'DateTimeField'},
        {label:'Date', id: 'DateField'},
        {label:'Boolean', id: 'DecimalField'},
        {label:'Email', id: 'EmailField'},
        {label:'ForeignKey', id: 'ForeignKey'},
        {label:'Integer', id: 'IntegerField'},
        {label:'Positive Integer', id: 'PositiveIntegerField'}];

    $scope.cancel = function () {
        $rootScope.newField = undefined;
        $scope.modalInstance.close();
    };
    $scope.ok = function () {
        if (scope.have_admin){
            scope.fieldAttribute.admin = scope.admin;
        };
        if (scope.have_serializer){
            scope.fieldAttribute.serializer = scope.serializer;
        };

        $rootScope.newField = scope.fieldAttribute;
        if ($rootScope.newField.name === ''){
            $rootScope.newField = undefined;
        }
        $scope.modalInstance.close();
    };

    scope.update = function (){
        if ($rootScope.newField  != undefined && $rootScope.newField .name != ''){
            scope.fieldAttribute =  $rootScope.newField;
            scope.admin = scope.fieldAttribute.admin;
            scope.serializer = scope.fieldAttribute.serializer;
            scope.have_admin = true;
            scope.have_serializer = true;
        }
    };
    scope.update();
}
angular
    .module('sbAdminApp')
    .controller('AddFieldCtrl', AddFieldCtrl);