from django.db import models
from .managers import StudentManager, MaleManager, FemaleManager, StudentModifyManager, StudentQuerySet
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.utils.encoding import smart_text

# Create your models here.

SEMESTER = (
    ('sem1', 'sem1'),
    ('sem2', 'sem2'),
    ('sem3', 'sem3'),
    ('sem4', 'sem4'),
)
GENDER = (
    ('male', 'male'),
    ('female', 'female'),
    ('others', 'others'),
)

class Hobby(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):

    MEDIA_CHOICES = [
        ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
        ),
        ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
        ),
        ('unknown', 'Unknown'),
    ]

    user_id = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    semester = models.CharField(
        choices=SEMESTER, default=SEMESTER[0][0], max_length=100)
    enroll_num = models.PositiveIntegerField(primary_key=True, validators=[
                                             MaxValueValidator(9999999999999)])
    gender = models.CharField(
        choices=GENDER, default=GENDER[0][0], max_length=100)
    registered_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    email = models.EmailField(max_length=254)
    media_choice = models.CharField(
        choices=MEDIA_CHOICES, null=True, max_length=100)
    profile_pic = models.ImageField(max_length=255, null=True,blank=True)
    password = models.CharField(max_length=128, null=True)
    hobbies = models.ManyToManyField(Hobby)
    class_teacher = models.ForeignKey(Teacher,null=True,on_delete=models.CASCADE)

    student = models.Manager()
    objects = StudentManager()
    male = MaleManager()
    female = FemaleManager()
    modify = StudentModifyManager()
    custom = StudentModifyManager.from_queryset(StudentQuerySet)()
    query = StudentQuerySet.as_manager()

    def __str__(self):
        return smart_text(self.name)
