from django.contrib import admin
from common.models import *
from django_json_widget.widgets import JSONEditorWidget


admin.site.register(Customer)
admin.site.register(Country)
admin.site.register(CustomUser)
admin.site.register(DocumentSet)
admin.site.register(CustomerDocument)

