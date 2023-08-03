from django.db import models
from accounts.models import People

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


# Course Model:
# course_num: CharField - state course code
# name: CharField to store the name of the course.
# description: TextField to provide a description of the course.
# department: ForeignKey to department model (related_name = "course")
# credits: PositiveIntergerField (max_length=1)
# is_active: BooleanField

class Course(models.Model):
    course_num = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    description = models.TextField()
    department = models.ForeignKey(Department, related_name="course", on_delete=models.CASCADE)
    credits = models.PositiveIntegerField()
    is_active = models.BooleanField(default=False,)
    prerequisite = models.ManytoManyField(
        "self",
        through="Prerequisite",
        symmetrical=False,
        through_fields=("course", "prerequisite")
    )


    def __str__(self):
        return f"Course: {self.name} {self.course_num}"




# Room Model:
# room_num: CharField
# building: CharField
# capacity: PositiveIntergerField
# teacher: ForeignKey, null

class Room(models.Model):
    room_num = models.CharField(max_length=10)
    building = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    teacher = models.ForeignKey(People.Teacher, on_delete=models.CASCADE, related_name="room_num",)

    def __str__(self):
        return self.room_num


# Prerequisite Model:
# - prerequisite_for: ForeignKey to the Course model to represent the course that the prerequisite is required for
# - name

class Prerequisite(models.Model):
    prerequisite = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course",
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="prerequisite",
        null=True,
    )
    name = models.CharField(max_length=200)
    column1 = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


# Section Model:
# course: ForeignKey to the Course model to represent the course associated with the session.
# teacher: ForeignKey to the Teacher model to represent the teacher assigned to the session.
# room: ForeignKey to the Room model to represent the room assigned to the session.
# period: ForeignKey
# semester: CharField
# capacity: PositiveIntergerField

class Section(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="section",
    )
    teacher = models.ForeignKey(
        People.Teacher,
        related_name="section",
        on_delete=models.SET_NULL,
        null=True,
    )
