from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
  model = CustomUser
  list_display = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'profile_image')
  fieldsets = UserAdmin.fieldsets + (
      (None, {'fields': ('bio', 'profile_image')}),
  )
  add_fieldsets = UserAdmin.add_fieldsets + (
      (None, {'fields': ('bio', 'profile_image')}),
  )


# Register the custom user model with the admin interface
admin.site.register(CustomUser, CustomUserAdmin)
