from django.contrib import admin

# Register your models here.
from .models import Student, Hobby, Teacher


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ['registered_date']

    class Meta:
        model = Student

    # def has_change_permission(self, request, obj=None):
    #     if obj is not None and (obj.user_id == request.user or request.user.has_perm('student.2_student_can_do_all_crud_permission')):
    #         return True
    #     return False
       
admin.site.register(Student, StudentAdmin)
admin.site.register(Hobby)
admin.site.register(Teacher)
