from django.contrib import admin
from .models import SendMail


# from django.utils.html import format_html
# from django.core.urlresolvers import reverse

class DesignAdmin(admin.ModelAdmin):
    list_display = ['id', 'namereceiver', 'receiver', 'subject']


admin.site.register(SendMail, DesignAdmin)
