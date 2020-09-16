from django.contrib import admin
from django.db import models
from django.forms import TextInput

from import_export.admin import ImportExportModelAdmin

from .models import Contact


class ContactAdmin(ImportExportModelAdmin):
    list_display = ('name', 'gender', 'email', 'info', 'phone',)
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name', 'phone', 'email', 'info', 'gender')
    list_filter = ('gender', 'info', 'date')

    formfield_overrides = {
        models.CharField : {'widget' : TextInput(attrs={'autocomplete' : 'off', 'class':'vTextField'})}
    }


admin.site.register(Contact, ContactAdmin)


# Admin Site Customization
admin.site.site_header = 'Contacts'
admin.site.index_title = 'Contact Administator'
admin.site.site_title = 'Control Panel'