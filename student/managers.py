
from django.db.models import Manager, Q, Sum, QuerySet,Max, Avg, Count
from datetime import datetime


class StudentManager(Manager):
    def get_total_students(self):
        return self.all().count()

    def get_avg_age_students(self):
        return self.aggregate(Avg('age'))

    def get_max_age_student(self):
        return self.aggregate(Max('age'))

    def get_students_age_less_or_equal(self, age):
        return self.filter(age__lte=age)

    def get_male_students_age_less_or_equal(self, age):
        return self.filter(gender='male').get_students_age_less_or_equal(age)

    def get_female_students_age_less_or_equal(self, age):
        return self.filter(gender='female', age__lte=age)

    def get_today_registered_students(self):
        return self.filter(registered_date=datetime.now())

    def get_sem3_or_sem4_students(self):
        return self.filter(Q(semester='sem3') | Q(semester='sem4'))

    def get_students_semester_age(self, sem, age):
        return self.filter(semester=sem, age__gte=age)

    def get_males(self):
        return self.filter(gender='male')

    def get_females(self):
        return self.filter(gender='female')


class MaleManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(gender='male')


class FemaleManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(gender='female')

# defining  Custom Querysets methods for the manager


class StudentQuerySet(QuerySet):
    def male(self):
        return self.filter(gender='male')

    def female(self):
        return self.filter(gender='female')

    def age_greater_or_equal_to(self, age):
        return self.filter(age__gte=age)

    def age(self):
        return self.filter(age=23)

# Defining Managers for implementing our StudentQueryset class methods


class StudentModifyManager(Manager):

    def get_student_manager_queryset(self):
        return StudentManager(self.model, using=self._db)

    def get_queryset(self):
        return StudentQuerySet(self.model, using=self._db)  # Important

    # male , female, age_greater_or_equal_to are chainable as they inherit the queryset
    #  methods of StudentQuerySet
    def male(self):
        return self.get_queryset().male()

    def female(self):
        return self.get_queryset().female()

    def age_greater_or_equal_to(self, age):
        return self.get_queryset().age_greater_or_equal_to(age)

    # below method is not chainable
    def get_sem3_students(self):
        return self.filter(semester='sem3')

    def get_today_registered_students(self, age):
        return self.get_student_manager_queryset().get_today_registered_students(age)
