from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import escape, mark_safe


User = get_user_model()

class UserAdministration(UserAdmin):
  
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 
                    )  # Campos que se mostrarán en el listado
    search_fields = ('username', 'email', 'first_name', 'last_name')  # Campos en los que puedes buscar
    list_filter = ('is_staff', 'is_active','is_student','is_teacher')  # Filtros que puedes agregar

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email","thumbnail","profile_image",'is_teacher','is_student',)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

     # Campos disponibles al crear un nuevo usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email','usable_password', 'password1', 'password2', 'first_name', 'last_name','is_staff','is_teacher','is_student','is_superuser','is_active'),
        }),
    )

    readonly_fields = ['thumbnail']

    def thumbnail (self, obj):
        return mark_safe('<img src="{url}" width="180" height="180" />'.format(
            url = obj.profile_image.url,
            width=obj.profile_image.width,
            height=obj.profile_image.height,
            )
    )

    class Media:
        js = ('js/admin_user_toggle.js',)  # Ruta relativa a tu carpeta static


# Register your models here.

admin.site.register(User, UserAdministration)