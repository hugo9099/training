/**
 * Created by yanspineiro on 5/27/16.
 */
var factories = angular.module('factories', ['ngResource']);
var apiPath = '/crm/api/v1';
var resourceGenerator = function(path, parameter = {}, isArray = false) {

    return function($resource) {
        return $resource(path, parameter,
            {
                'update': { method:'PUT' },
                'patch' : { method: 'PATCH' },
                'query': {method:'GET', isArray: isArray}
            });
    }
};

factories.factory('testtt', function($resource){
    return $resource(apiPath + '/training/FieldType/', {}, {
        query: {
            method: 'GET'
        }
    });
});

factories.factory('Generate', function($resource){
    return $resource(apiPath + '/training/build-class/', {}, {
        query: {
            method: 'GET'
        }
    });
});
