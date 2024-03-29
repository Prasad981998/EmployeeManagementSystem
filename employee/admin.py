from django.contrib import admin
from .models import Role,Department,Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','dept','salary','bonus','role','phone','hire_date']

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['id','name','location']
