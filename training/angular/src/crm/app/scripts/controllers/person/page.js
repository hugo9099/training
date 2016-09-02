/**
 * Created by yanspineiro on 7/15/16.
 */
function PersonCtrl($rootScope, $interval, $window, $scope, $modal) {
    let scope = this;
    var pageSize = 12;
    var page = 1;
    scope.search_string = '';
    scope.itemList = [];
    $scope.previousPage = null;
    $scope.nextPage = null;
    $scope.total_rows = 0;



    scope.search = function (option) {

        scope.params = {limit: pageSize, search_string: ''};

        if (scope.search_string.length !== 0) scope.params.search_string = scope.search_string;

        page = option === 1 ? 1 : page;
        scope.params.offset = (page - 1) * pageSize;
        scope.params.limit = pageSize;
        scope.params.offset = scope.params.offset < 0 ? 0 : scope.params.offset;


        //PersonMgr.query(scope.params, function (r) {
        //    scope.itemList = r.rows;
        //    //$scope.nextPage = r.total_row;
        //    $scope.previousPage = scope.params.offset === pageSize ? 0 :1 ;
        //    $scope.nextPage = scope.params.offset < r.total_row ? 1 :0 ;
        //    $scope.total_rows = r.total_row;
        //});

    };

    scope.clearFilters = function () {

        scope.search_string = '';
        scope.user_list = [];
        scope.nextPage = null;
        scope.previousPage = null;
        $scope.total_rows = 0;


    };

    scope.addItem = function () {

        ItemModalInstance = $modal.open(
            {
                templateUrl: 'views/person/add.html',
                controller: function($modalInstance, $scope){
                    $scope.modalInstance = $modalInstance;
                    return AddPersonCtrl;
                },
                size:'lg'
            }
        );
    };


}
angular
    .module('sbAdminApp')
    .controller('PersonCtrl', PersonCtrl);


