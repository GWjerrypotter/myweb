from django.contrib import admin
from officialweb.models import *


@admin.register(Docs)
class DocsAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all.js',
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/config.js',
        )


# admin.site.register(Docs)
admin.site.register(DocType)
