from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
from .utils import generate_groups_and_permission
from django.contrib.contenttypes.models import ContentType
# from project_calendars.models import CalendarBriefMapping
from .permission_constant import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


@receiver(post_save, sender=Student)
def create_groups_for_project(sender, instance, **kwargs):
    print("---------ender-------", sender,
          "--------instance--------", instance)
    print("-----------ags----------", kwargs)
    if kwargs['created']:
        try:
            temp = User.objects.filter(email=instance.email)
            if not temp:
                content_type = ContentType.objects.get(
                    model=instance._meta.model_name)
                print("------content_type---------", content_type)
                generate_groups_and_permission(instance._meta.model_name,
                                            str(instance.enroll_num), content_type)

                super_group = Group.objects.get(
                    name=str(instance.enroll_num) + STUDENT_SUPER_GROUP)
                view_group = Group.objects.get(
                    name=str(instance.enroll_num) + STUDENT_VIEW_ONLY_GROUP)

                print("----------super_group--------", super_group)
                print("----------view_group--------", view_group)
            
                temp = User.objects.create(
                    username=instance.name,
                    email=instance.email,
                )
            print("---user--create----", temp)
            print("---user--create----", instance.user_id)
            print("---user--create---age>>>>>-", instance.age)

            if not instance.user_id:
                new_stu = Student.objects.filter(enroll_num=instance.enroll_num)
                print("-----new-------stu-------", new_stu)
                Student.objects.filter(
                    enroll_num=instance.enroll_num).update(user_id_id=temp.id)
            # instance.user_id_id = User.objects.get(pk=temp.id)
            # print("------instance.user_id-----------",new_stu.user_id)
                temp.groups.add(super_group)
            # instance.client.user_id.groups.add(view_group)

        except Exception as e:
            raise e
    else:
        print("Object not created yet.")
