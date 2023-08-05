from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet


class Department(models.Model):
    name = models.CharField(max_length=100,)
    description = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):

    class ActiveCourses(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filer(is_active=True)

    course_code = models.CharField(max_length=50,)
    name = models.CharField(max_length=150)
    description = models.TextField()
    department = models.ForeignKey(
        Department,
        related_name="course",
        on_delete=models.CASCADE,
    )
    credits = models.PositiveIntegerField(max_length=1,)
    is_active = models.BooleanField(default=False,)
    prereqs = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name="prereqs",
    )

    objects = models.Manager() # default manager
    activecourses = ActiveCourses() # custom manager

    def __str__(self):
        return self.course_code
