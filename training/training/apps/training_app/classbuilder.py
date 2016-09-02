from django.db import models

TYPE_Choice = {'TEXT': 'CharField',
               'DateTime': 'DateTimeField',
               'Date': 'DateField',
               'Boolean': 'BooleanField',
               'Coma Separate Integer': 'CommaSeparatedIntegerField',
               'Decimal': 'DecimalField',
               'Email': 'EmailField',
               'ForeignKey': 'ForeignKey',
               'Integer': 'IntegerField',
               'Positive Integer': 'PositiveIntegerField'

               }


class builderClass:
    def __init__(self, name=None, fields=[]):

        if name != None:
            self.map_class = {'Name': name, 'fields': fields}

        # self.map_class = {'Name': '',
        #                   'fields': []
        #                   }
        self.admin = {'isdisplayname': False,
                      'is_searchfield': False,
                      'is_filter': False,
                      'is_readOnly': False
                      }
        self.serializer = {'allow_blank': True,
                           'default': '',
                           'source': '',
                           'max_length': '',
                           'required': False
                           }
        self.field = {'name': '',
                      'dataType': '',
                      'default': '',
                      'blank': False,
                      'null': True,
                      'auto_now_add': False,
                      'max_length': '',
                      'verbose_name': '',
                      'ForeignKey': '',
                      'primary_key': False,
                      'display': False,
                      'admin': self.admin,
                      'serializer': ''
                      }

    def generate_class(self):
        va = ''
        template_class = """ class {} (models.Model):
                            """.format(self.map_class.get('Name'))
        template_constructor = """ def __str__(self):
                                    return {} """
        field_list = self.map_class.get('fields')
        list_field_format = []
        list_display = []
        for item in field_list:
            field_item = {}
            for key in self.field:
                if 'admin' != key and 'display' != key and 'serializer' != key:
                    value = item.get(key)
                    if value:
                        field_item[key] = value

                if 'display' in key and item.get(key):
                    list_display.append('self.{}'.format(item.get('name')))

            if field_item:
                datatype = field_item.get('dataType')
                # if datatype:
                #     if TYPE_Choice.get(datatype):
                #         field_item['type'] = 'model.{}'.format(TYPE_Choice.get(datatype))
                # else:
                #     field_item['type'] = 'model.CharField'
                template_field = "{} = {}(property)  \n".format(field_item['name'], field_item['dataType'])
                field_item.pop('name', 0)
                field_item.pop('dataType', 0)
                propertys = ''
                if field_item:
                    propertys = ",".join(str('{}={}').format(key, value) for key, value in field_item.iteritems())
                template_field = template_field.replace('property', propertys)
                template_class += template_field
                # list_field_format.append(field_item)

        if list_display:
            value = ','.join(list_display)
            template_constructor = template_constructor.format(value)
        else:
            template_constructor = template_constructor.format('id')

        return template_class + """ \n """ + template_constructor

    def generate_admin(self):
        class_name = self.map_class.get('Name')
        template_class = """@admin.register(models.{})
                            class {}Admin(admin.ModelAdmin):
                                {}
                                {}
                                {}
                                {}
                                list_per_page = 25
                                """
        field_list = self.map_class.get('fields')
        list_disp = []
        search_field = []
        # list_display_links = []
        readonly_fields = []
        list_filter = []
        for field in field_list:
            admin_field = field['admin']
            field_name = field['name']
            if admin_field['isdisplayname']:
                list_disp.append("'{}'".format(field_name))
            if admin_field['is_searchfield']:
                search_field.append("'{}'".format(field_name))
            if admin_field['is_filter']:
                list_filter.append("'{}'".format(field_name))
            if admin_field['is_readOnly']:
                readonly_fields.append("'{}'".format(field_name))

        display = ''
        search = ''
        read_only = ''
        filter_field = ''
        if list_disp:
            display = "list_display = ({})".format(','.join(list_disp))
        if search_field:
            search = "search_fields = ({})".format(','.join(search_field))
        if list_filter:
            filter_field = "list_filter = ({})".format(','.join(list_filter))
        if readonly_fields:
            read_only = "readonly_fields = ({})".format(','.join(readonly_fields))

        template_class = template_class.format(class_name, class_name, display, search, read_only, filter_field)
        return template_class

    def generate_serializer(self):
        val = ""
        template_class = """class {}Serializer(serializers.ModelSerializer):
                           {}"""
        class_meta = """class Meta:
                            model = {}""".format(self.map_class.get('Name'))
        field_list = self.map_class.get('fields')
        fields_formated = []
        for field in field_list:
            serializer_field = field['serializer']
            field_name = field['name']
            data_type = field.get('dataType')
            properties = []

            for key, value in serializer_field.iteritems():
                if 'bool' in str(type(value)):
                    properties.append('{}= {}'.format(key, value))
                elif value:
                    properties.append('{}= {}'.format(key, value))
            field_propertys = ','.join(properties)
            fields_formated.append('{} = serializers.{}({})'.format(field_name, data_type, field_propertys))
        fields_formated.append(class_meta)
        all_field = "\n".join(fields_formated)
        template_class = template_class.format(self.map_class.get('Name'), all_field)
        return template_class

    def generate_viewset(self):

        class_name = self.map_class.get('Name')
        template_class = """ class {}ViewSet(viewsets.ModelViewSet):
                                    model = {}
                                    serializer_class = {}Serializer
                                    queryset = {}.objects.all()


        """.format(class_name, class_name, class_name, class_name)
        template_filter_backends = """"({})"""
        search = 'filters.SearchFilter'
        ordering = 'filters.OrderingFilter'
        filterbackend = 'filters.DjangoFilterBackend'

        template_def = """def list(self, request, *args, **kwargs):
                                return super({}ViewSet, self).list(request, *args, **kwargs)""".format(class_name)
        template_search = """search_fields = ({})"""

        template_ordering = """ordering_fields = ({})"""

        template_filter = """filter_fields = ({})"""

        list_search = []
        list_ordering = []
        list_filter = []
        list_backend = []

        field_list = self.map_class.get('fields')
        for field in field_list:
            admin_field = field['admin']
            field_name = field['name']
            if admin_field.get('is_searchfield'):
                list_search.append(field_name)
            if admin_field.get('is_filter'):
                list_filter.append(field_name)

        if len(list_search) > 0:
            list_backend.append(search)
            template_search = template_search.format(','.join(list_search))
        else:
            template_search = ''

        if len(list_ordering) > 0:
            list_backend.append(ordering)
            template_ordering = template_ordering.format(','.join(list_ordering))
        else:
            template_ordering = ''

        if len(list_filter) > 0:
            list_backend.append(filterbackend)
            template_filter = template_filter.format(','.join(list_filter))
        else:
            template_filter = ''

        if len(list_backend) > 0:
            template_filter_backends = template_filter_backends.format(','.join(list_backend))

        return '{} \n {} \n {} \n {} \n {} \n {}'.format(template_class, template_filter_backends, template_search,
                                                         template_ordering, template_filter, template_def)

    def generate_url(self):
        class_name = self.map_class.get('Name')
        template = """ router.register(r'{}', views.{}ViewSet)""".format(class_name.lower(), class_name)
        return template
