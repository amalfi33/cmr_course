from django.contrib import admin
from .models import Group , Course , Employee
# Register your models here.

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Employee)

