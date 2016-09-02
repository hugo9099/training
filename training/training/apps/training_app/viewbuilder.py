CHOICE_INPUT = {'CharField': """<div class="form-group ">
                                    <label class="col-sm-4 control-label">{}</label>
                                    <div class="col-sm-6">
                                    <input type="text" ng-model="add{}Ctrl.attributes.{}"
                                    name="field{}"
                                    class="form-control">
                                    </div>
                                    </div>

                                """,
                'DateTimeField': '',
                'DateField': '',
                'BooleanField': """<div class="form-group">
                                    <div><label class="col-sm-5 control-label">{}
                                        <input type="checkbox" ng-model="add{}Ctrl.attributes.{}"
                                        name="field{}>
                                        </label></div>
                                """,
                'CommaSeparatedIntegerField': """
                                                <div class="form-group">
                                                <label>{}</label>
                                                <textarea class="form-control" rows="10"
                                                ng-model="add{}Ctrl.attributes.{}"
                                                name="field{}>
                                                </textarea>
                                                </div>
                                                """,
                'DecimalField': """<div class="form-group ">
                                    <label class="col-sm-4 control-label">{}</label>
                                    <div class="col-sm-6">
                                    <input type="email" ng-model="add{}Ctrl.attributes.{}"
                                    name="field{}"
                                    class="form-control">
                                    </div>
                                    </div>

                                """,
                'EmailField': """<div class="form-group ">
                                    <label class="col-sm-4 control-label">{}</label>
                                    <div class="col-sm-6">
                                    <input type="email" ng-model="add{}Ctrl.attributes.{}"
                                    name="field{}"
                                    class="form-control">
                                    </div>
                                    </div>

                                """,
                'ForeignKey': """<div class="form-group">
                                    <label class="col-sm-4 control-label">{}</label>

                                    <div class="col-sm-6">
                                    <select class="form-control"
                                    ng-model="add{}trl.attribute.{}"
                                    required>
                                    <option ng-repeat="item in add{}Ctrl.{}"
                                        value="{{item.id}}">{{item.label}}
                                    </option>
                                     </select>
                                 </div>
                                </div>

                                """,
                'IntegerField': """<div class="form-group ">
                                    <label class="col-sm-4 control-label">{}</label>
                                    <div class="col-sm-6">
                                    <input type="text" ng-model="add{}Ctrl.attributes.{}"
                                     name="field{}"
                                    class="form-control">
                                    </div>
                                    </div>

                                """,
                'PositiveIntegerField': """<div class="form-group ">
                                    <label class="col-sm-4 control-label">{}</label>
                                    <div class="col-sm-6">
                                    <input type="text" ng-model="add{}Ctrl.attributes.{}"
                                     name="field{}"
                                    class="form-control">
                                    </div>
                                    </div>

                                """,
                'Choice': """ <div class="form-group">
                        <label class="col-sm-4 control-label">{}</label>

                        <div class="col-sm-6">
                            <select class="form-control"
                                    ng-model="add{}trl.attribute.{}"
                                    required>
                                <option ng-repeat="item in add{}Ctrl.{}"
                                        value="{{item.id}}">{{item.label}}
                                </option>
                            </select>
                        </div>
                    </div>"""

                }


def generate_html_page(field_list, class_name):
    th = ' '.join("<th>{}</th>".format(field.get('name').title()) for field in field_list)

    template_body = """
    <div class="wrapper wrapper-content animated fadeInRight" ng-controller="{}Ctrl as {}Ctrl">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-12">
                     <div class="panel-heading">
                        <button type="button" class="btn btn-success" ng-click="{}Ctrl.addItem()"><i class="fa fa-plus"></i></button>
                        {}
                     </div>
                    <div class="panel panel-default">
                        <div class="panel-body">
                            <div class="table-responsive">
                                <table class="table">
                                  {}
                                  {}
                                 </table>
                             </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


    """
    thead_template = """
                            <thead>
                                <tr>
                                    <th></th>
                                    {}
                                </tr>
                                </thead>
    """
    td = ' '.join(" <td>{{item.{} }}</td> ".format(field.get('name').lower()) for field in field_list)
    tbody_template = """"
                <tbody>
                    <tr ng-repeat="item in {}Ctrl.itemList">
                        <td><a ng-click="{}Ctrl.update(item)" title="Edit"><i
                            class="fa fa-pencil text-navy"></i> </a></td>
                           {}
                    </tr>

                </tbody>
     """
    class_name_lower = class_name.lower()
    class_name_title = class_name.title()
    thead_template = thead_template.format(th)
    tbody_template = tbody_template.format(class_name_lower, class_name_lower, td)

    template_body = template_body.format(class_name_title, class_name_lower, class_name_lower, class_name_title,
                                         thead_template, tbody_template)
    return template_body


def generate_html_add(fields, class_name):
    template_add = """
    <div class="modal-body" ng-controller="Add{}Ctrl as add{}Ctrl" >
        <div class="row">
            <h5>Add new {}</h5>
        </div>

        <div class="ibox-content" >
            <form method="post" class="form-horizontal ng-pristine ng-valid">
                <div class="row">
                {}
                </div>
                <div class="row">
                    <br/>

                    <div class="form-group">
                        <div class="text-center">
                            <button class="btn btn-sm btn-primary m-t-n-xs" style="width: 80px" ng-click="ok()">
                            <strong>Save</strong>
                            </button>
                            <button class="btn btn-sm btn-white m-t-n-xs" style="width: 80px" ng-click="cancel()">
                            <strong>Cancel</strong></button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>

    """
    input_list = []
    classname_lower = class_name.lower()
    classname_title = class_name.title()
    for item in fields:
        name = item['name']
        name_title = name.title()
        name_lower = name.lower()
        datatype = item['dataType']
        choice = item.get('choice')
        template_input = CHOICE_INPUT[datatype]
        if choice:
            choice_value = item['choiceValue']
            template_input = CHOICE_INPUT['Choice'].format(name_title, classname_lower, name_lower, classname_lower,
                                                           choice_value)
        elif 'ForeignKey' in datatype:
            foreign_key = item['ForeignKey']
            template_input = template_input.format(name_title, classname_lower, name_lower, classname_lower,
                                                   foreign_key)


        elif template_input:
            template_input = template_input.format(name_title, classname_lower, name_lower, name_title)
        else:
            template_input = CHOICE_INPUT['CharField']
            template_input = template_input.format(name_title, classname_lower, name_lower, name_title)
        input_list.append(template_input)

    all_input = '\n'.join(input_list)

    template_add = template_add.format(classname_title, classname_lower, classname_title, all_input)
    return template_add


def generate_javascritp_add(field_list, class_name):
    template_choice = """
                $scope.{} = {}Srv.get{}();
                    if ($scope.{} !== undefined && $scope.{}[0].id === 0) $scope.{}.shift();
                        $rootScope.$on('{}SrvUpdated', function () {
                            var arr = {}Srv.get{}();
                            if (arr[0].id === 0) arr.shift();
                                 $scope.{} = arr;
                        });
                     """


    template_controller = """
    function Addclassname_titleCtrl($rootScope, $interval, $window, $scope, $modal,Addclassname_title,fact ) {
    var scope = this;
    template_new_item
    factory
    scope_ok
    $scope.cancel = function () {
        $scope.modalInstance.close();
    };
    }
    angular
    .module('MODULE')
    .controller('Addclassname_titleCtrl', Addclassname_titleCtrl)
    """
    classname_lower = class_name.lower()
    classname_title = class_name.title()

    scope_ok = """
    $scope.ok = function () {
        scope.extra_msg = '';
        var params = $.param(scope.new{classname_title});
        Add{classname_title}.add_{classname_title}(params, function (result) {
            if (result.success != undefined) {
                swal({ title: 'Submit', text: '{classname_title} created successfully!.', type: 'success' });
                $scope.modalInstance.close();
            }
            else {
                swal({ title: "Submit", text: 'Error saving {classname_title}', type: "error" });
            }

        });


    };"""

    scope_ok = scope_ok.replace('{classname_title}',classname_title)
    choice_factory_list = []
    map_field_list = []
    fact_list = []
    for item in field_list:
        name = item['name']
        name_title = name.title()
        name_lower = name.lower()
        datatype = item['dataType']
        choice = item.get('choice')
        if choice:
            choice_factory_list.append(template_choice.format(name_lower, name_title))
            fact_list.append(name_title)
        if 'ForeignKey' in datatype:
            choice_factory_list.append(template_choice.format(item['ForeignKey'].title()))
            fact_list.append(name_title)

        map_field_list.append("{} : null".format(name_lower))
    template_new_item = """ scope.attributes = { {} }"""

    fields = '\n'.join(map_field_list)
    factory = '\n'.join(choice_factory_list)
    template_new_item = template_new_item.replace('{}',fields)
    fact = ','.join(fact_list)
    template_controller = template_controller.replace('classname_title',classname_title)
    template_controller = template_controller.replace('template_new_item', template_new_item)
    template_controller = template_controller.replace('factory', factory)
    template_controller = template_controller.replace('fact', fact)
    template_controller = template_controller.replace('scope_ok', scope_ok)
    return template_controller



def generate_javascritp_html_page(field_list, class_name):
    print class_name
    # itemList
    # addItem()
    # filters
    # search_srt
    #  Class_name_title,   Class_name_title , factory&Choices tittle, selectedfactory&Choices lower  ,template_selected, Class_name_title ,template_clear_filter
    # # template_filter   ,Class_name_.lower    ,Class_name_.lower,Class_name_title ,Class_name_title,Class_name_title
    # (, , , , ,
    #                            , ,
    #                            , , , classname_title, classname_title,
    #                            )

    template = """ function {classname_title}MgrCtrl($rootScope, $interval, $window, $scope, $modal, {classname_title}Mgr, {factorys}) {
    let scope = this;
    var pageSize = 12;
    var page = 1;
    scope.search_string = '';
    scope.itemList = [];
    $scope.previousPage = null;
    $scope.nextPage = null;
    $scope.total_rows = 0;
    {template_selected}
    {promesas}

      scope.search = function (option) {

        scope.params = {limit: pageSize, search_string: ''};
        {template_filter}
        if (scope.search_string.length !== 0) scope.params.search_string = scope.search_string;

        page = option === 1 ? 1 : page;
        scope.params.offset = (page - 1) * pageSize;
        scope.params.limit = pageSize;
        scope.params.offset = scope.params.offset < 0 ? 0 : scope.params.offset;


        {classname_title}Mgr.query(scope.params, function (r) {
            scope.itemList = r.rows;
            //$scope.nextPage = r.total_row;
            $scope.previousPage = scope.params.offset === pageSize ? 0 :1 ;
                $scope.nextPage = scope.params.offset < r.total_row ? 1 :0 ;
            $scope.total_rows = r.total_row;
        });

    };

       scope.clearFilters = function () {

        scope.search_string = '';
        scope.user_list = [];
        scope.nextPage = null;
        scope.previousPage = null;
        $scope.total_rows = 0;
        {template_clear_filter}

           };

        scope.addItem = function () {

            ItemModalInstance = $modal.open(
               {
                   templateUrl: 'views/{classname_lower}/add_{classname_lower}.html',
                   controller: function($modalInstance, $scope){
                       $scope.modalInstance = $modalInstance;
                       return Add{classname_title}Ctrl;
                   },
                   size:'lg'
               }
            );
        };


    }
    angular
        .module('MODULE')
        .controller('{classname_title}MgrCtrl', {classname_title}MgrCtrl);


           """

    #  Class_name_title,   Class_name_title , factory&Choices tittle, selectedfactory&Choices lower  ,template_selected, Class_name_title ,template_clear_filter
    # template_filter   ,Class_name_.lower    ,Class_name_.lower,Class_name_title ,Class_name_title,Class_name_title

    template_selected = """$scope.{}Selected"""
    template_filter = """ if ($scope.{}Selected !== undefine && $scope.{}Selected !== '')
                          scope.params.{} = $scope.{}Selected;"""
    template_clear_filter = """ $scope.{}Selected = null;"""
    template_choice = """
                $scope.{} = {}Srv.get{}();
                    if ($scope.{} !== undefined && $scope.{}[0].id === 0) $scope.{}.shift();
                        $rootScope.$on('{}SrvUpdated', function () {
                            var arr = {}Srv.get{}();
                            if (arr[0].id === 0) arr.shift();
                                 $scope.{} = arr;
                        });
                     """

    list_selected = []
    list_filter = []
    list_clear_fitler = []
    list_fact = []

    for item in field_list:
        name = item['name']
        name_title = name.title()
        name_lower = name.lower()
        datatype = item['dataType']
        choice = item.get('choice')
        if choice or 'ForeignKey' in datatype:
            list_selected.append(template_selected.format(name_title))
            list_filter.append(template_filter.format(name_lower, name_lower, name_lower, name_lower, name_lower))
            list_clear_fitler.append(template_clear_filter.format(name_lower))
            list_fact.append(name_title)

    template_selected = '\n'.join(list_selected)
    template_filter = '\n'.join(list_filter)
    template_clear_filter = '\n'.join(list_clear_fitler)
    factorys = ','.join(list_fact)
    classname_lower = class_name.lower()
    classname_title = class_name.title()
    promesas = ''

    # template = template.format(classname_title, classname_title, factorys, template_selected, promesas,
    #                            classname_title, template_clear_filter,
    #                            template_filter, classname_lower, classname_lower, classname_title, classname_title,
    #                            classname_title)
    template = template.replace('{classname_title}', classname_title)
    template = template.replace('{factorys}', factorys)
    template = template.replace('{template_selected}', template_selected)
    template = template.replace('{template_clear_filter}', template_clear_filter)
    template = template.replace('{template_filter}', template_filter)
    template = template.replace('{classname_lower}', classname_lower)
    template = template.replace('{promesas}', promesas)

    return template
