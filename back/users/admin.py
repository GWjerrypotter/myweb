from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users import models
from users.models import Users


class UsersModels(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'user_name', 'dept', 'user_phone', 'user_remark', 'groups')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      )}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        # 'groups', 'user_permissions'
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'user_name', 'is_staff',
                       'dept', 'user_phone', 'user_remark', 'groups')
        }),
    )

    list_display = ('id', 'username', 'user_name', 'dept', 'user_phone', 'user_remark')


admin.site.register(Users, UsersModels)
admin.site.register(models.DeptMent)

