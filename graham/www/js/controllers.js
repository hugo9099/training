angular.module('starter.controllers', [])

  .controller('AppCtrl', function ($scope, $ionicModal, $timeout, $http, service) {

    // With the new view caching in Ionic, Controllers are only called
    // when they are recreated or on app start, instead of every page change.
    // To listen for when this page is active (for example, to refresh data),
    // listen for the $ionicView.enter event:
    //$scope.$on('$ionicView.enter', function(e) {
    //});

    $scope.symbol = "AAPL";
    //Book Price Multiplier
    $scope.bpm = 1.5;
    //Book Value per Share
    $scope.bvps = 0.00;
    //Earnings Multiplier
    $scope.em = 15;
    //Earnings Per Share
    $scope.eps = 0.00;
    //Price Per Share
    $scope.pps = 0.00;
    //graham number
    $scope.gn=  0.00;
    $scope.valuation=  0.00;

    $scope.items = [];
    $scope.startDate = '2016-06-24';
    $scope.endDate = '2016-06-24';
    // Form data for the login modal
    $scope.loginData = {};

    // Create the login modal that we will use later
    $ionicModal.fromTemplateUrl('templates/login.html', {
      scope: $scope
    }).then(function (modal) {
      $scope.modal = modal;
    });

    // Triggered in the login modal to close it
    $scope.closeLogin = function () {
      $scope.modal.hide();
    };

    // Open the login modal
    $scope.login = function () {
      $scope.modal.show();
    };

    // Perform the login action when the user submits the login form
    $scope.doLogin = function () {
      console.log('Doing login', $scope.loginData);

      // Simulate a login delay. Remove this and replace with your login
      // code if using a login system
      $timeout(function () {
        $scope.closeLogin();
      }, 1000);
    };
    $scope.search = function () {
      $scope.items = [];
      $scope.bpm = 1.5;
      $scope.bvps = 0.00;
      $scope.em = 15;
      $scope.eps = 0.00;
      $scope.pps = 0.00;

      var promise = service.getHistoricalData($scope.symbol);//$scope.startDate, $scope.endDate

      promise.then(function (data) {
        $scope.items = data;
        if (data != undefined && data.stats != undefined) {
          $scope.bvps = data.stats.BookValuePerShare.content != undefined ? parseFloat(data.stats.BookValuePerShare.content) : 0;
          $scope.eps = data.stats.DilutedEPS.content != undefined ? parseFloat(data.stats.DilutedEPS.content) : 0;
          $scope.pps = data.stats.P_50DayMovingAverage != undefined ? parseFloat(data.stats.P_50DayMovingAverage) : 0;


        }


      });

    };
    $scope.decimalFP = function (fpNum,d) {
// This function will format a floating point number to show the desired number of decimal places.

      fpNum = Math.round(fpNum*Math.pow(10,d))/Math.pow(10,d);
      str = fpNum.toString();
      i = str.indexOf(".");
      if (i>-1) {
        dif = str.length - i;
        while (dif<(d+1)) {
          str += "0";
          dif = str.length - i;
        }
      } else {
        str += ".";
        for (k=0;k<d;k++) {
          str += "0";
        }
      }
      return str;
    };

    $scope.calcGraham = function () {
      var factor1 = parseFloat($scope.bpm);
      var factor2 = parseFloat($scope.em);
      var BVPS = parseFloat($scope.bvps);
      var EPS = parseFloat($scope.eps);
      var PPS = parseFloat($scope.pps);

      var graham = Math.pow(factor1*factor2*EPS*BVPS,0.5);
      $scope.gn = parseFloat($scope.decimalFP(graham,2));
      if (PPS > graham) {
        // overvalued
        var value = (PPS-graham)/graham;
        $scope.valuation = parseFloat("+"+$scope.decimalFP(value*100,2)+"%");
      } else {
        // undervalued
        var value = (graham-PPS)/graham;
        $scope.valuation = parseFloat("-"+$scope.decimalFP(value*100,2)+"%");
      }

    };


  })

  .controller('PlaylistsCtrl', function ($scope) {
    $scope.playlists = [
      {title: 'Reggae', id: 1},
      {title: 'Chill', id: 2},
      {title: 'Dubstep', id: 3},
      {title: 'Indie', id: 4},
      {title: 'Rap', id: 5},
      {title: 'Cowbell', id: 6}
    ];
  })

  .controller('PlaylistCtrl', function ($scope, $stateParams) {
  })
  .factory('service', function ($q, $http) {

    return {
      //, start, end
      getHistoricalData: function (symbol) {
        var deferred = $q.defer();
        //var format = '&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=JSON_CALLBACK';
        var format = '&format=json&env=http://dqydj.net/scripts/YQL/finance/tables.env&callback=JSON_CALLBACK';
        //var query = 'select * from yahoo.finance.historicaldata where symbol = "' + symbol + '" and startDate = "' + start + '" and endDate = "' + end + '"';
        var query = 'select * from yahoo.finance.keystats where symbol = "' + symbol + '"';

        var url = 'http://query.yahooapis.com/v1/public/yql?q=' + encodeURIComponent(query) + format;

        $http.jsonp(url).success(function (json) {
          var quotes = json.query.results;
          // filter + format quotes here if you want
          deferred.resolve(quotes);
        });
        return deferred.promise;
      }
    };
  });
