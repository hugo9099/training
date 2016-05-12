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


class builderclass:
    map_class = {'Name': '',
                 'fields': []
                 }
    admin = {'isdisplayname': False,
             'is_searchfield': False,
             'is_filter': False,
             'is_readOnly': False
             }
    field = {'name': '',
             'type': '',
             'default': '',
             'blank': False,
             'null': True,
             'auto_now_add': False,
             'max_length': '',
             'verbose_name': '',
             'ForeignKey': '',
             'primary_key': False,
             'display': False,
             'admin': admin
             }

    def generate_class(self):
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
                if 'admin' and 'display' not in key:
                    value = item.get(key)
                    if value:
                        field_item[key] = value

                if 'display' in key and item.get(key):
                    list_display.append('self.{}'.format(item.get('name')))

            if field_item:
                type = field_item.get('type')
                if type:
                  if TYPE_Choice.get(type):
                    field_item['type'] = TYPE_Choice.get(type)
                else:
                    field_item['type'] = 'CharField'
                template_field = "{} = {}(property)  \n".format(field_item['name'], field_item['type'])
                field_item.pop('name', 0)
                field_item.pop('type', 0)
                propertys = ''
                if field_item:
                    propertys = ",".join( str('{}={}').format(key, value) for key,value  in field_item.iteritems())
                template_field = template_field.replace('property',propertys)
                template_class += template_field
                # list_field_format.append(field_item)

        if list_display:
            value = ','.join(list_field_format)
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
                                """.format(class_name, class_name)
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
                list_disp.append(field_name)
            if admin_field['is_searchfield']:
                search_field.append(field_name)
            if admin_field['is_filter']:
                list_filter.append(field_name)
            if admin_field['is_readOnly']:
                readonly_fields.append(field_name)

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

        template_class = template_class.format(class_name, class_name, display, search, read_only, filter)
        return template_class











