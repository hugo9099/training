/**
 * Created by yanspineiro on 7/15/16.
 */

function AddPersonCtrl($rootScope, $interval, $window, $scope, $modal,AddPerson) {
    var scope = this;
    scope.attributes = { firstname : null,
        lastname : null,
        age : null }


    $scope.ok = function () {
        scope.extra_msg = '';
        var params = $.param(scope.newPerson);
        AddPerson.add_Person(params, function (result) {
            if (result.success != undefined) {
                swal({ title: 'Submit', text: 'Person created successfully!.', type: 'success' });
                $scope.modalInstance.close();
            }
            else {
                swal({ title: "Submit", text: 'Error saving Person', type: "error" });
            }

        });


    };
    $scope.cancel = function () {
        $scope.modalInstance.close();
    };
}
angular
    .module('sbAdminApp')
    .controller('AddPersonCtrl', AddPersonCtrl)
