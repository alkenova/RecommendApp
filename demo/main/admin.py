from django.contrib import admin
from main.models import Category, Product
from django.contrib.auth.models import User


# Register your models here.

admin.site.register(Category)
admin.site.register(Product)

# admin.site.unregister(User)
#
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#
#     def group(self, user):
#         groups = []
#         for group in user.groups.all():
#             groups.append(group.name)
#         return ' '.join(groups)
#
#     group.short_description = 'Groups'
#
#     list_display = ('id', 'username', 'group', 'is_superuser', 'password')

