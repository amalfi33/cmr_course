from django.contrib import admin
from .models import Group , Course , Employee, Teacher , Student , Attendance , Position
# Register your models here.

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Employee)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Position)


