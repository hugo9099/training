'use strict';
/**
 * @ngdoc overview
 * @name sbAdminApp
 * @description
 * # sbAdminApp
 *
 * Main module of the application.
 * (function () {
    angular.module('sbAdminApp', [
        'oc.lazyLoad',
        'ui.router',
        'ui.bootstrap',
        'angular-loading-bar',
        'factories',
    ])
})();
 */
//angular
//  .module('sbAdminApp', [
//    'oc.lazyLoad',
//    'ui.router',
//    'ui.bootstrap',
//    'angular-loading-bar',
//        'factories'
//  ]);


(function () {
    angular.module('sbAdminApp', [
        'ui.router',
        'factories',
        'oc.lazyLoad',
        'ui.bootstrap',
        'angular-loading-bar'

    ])
})();