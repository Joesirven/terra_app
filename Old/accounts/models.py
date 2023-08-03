from typing import Optional
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser, BaseUserManager
from course.models import Section
from schedules.models import Enrollment


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, phone, first_name, last_name, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of birth, and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, phone, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_superuser(email, date_of_birth, phone, first_name, last_name, password, **extra_fields)




class People(AbstractUser):
    date_of_birth = models.DateField()
    phone = PhoneField(unique=True, help_text="Phone number to send verification code to",)
    image = models.ImageField(upload_to="photos/")
    is_staff = models.BooleanField(default=False,)
    email = models.EmailField(unique=True,)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ["username", 'first_name', 'last_name', "phone", "date_of_birth",]


    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def has_perm(self, perm: str, obj: Optional[models.Model] = None) -> bool:
        return super().has_perm(perm, obj)

    def has_module_perms(self, app_label: str) -> bool:
        return super().has_module_perms(app_label)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    class Teacher(People):
        pass

    # Student Model
# 		- grade_level: PositiveIntegerField
# 		- dob: DateField
# 		- Student_id: CharField
# 		- Counselor: ForeignKey to Staff (related_name='students')
# 		- Enrollment: ManytoManyField(Section, through="Enrollment")


    class Student(People):
        grade_level = models.PositiveIntegerField(max_length=2)
        student_id = models.PositiveIntegerField(
            max_length=10,
        )
        counselor: models.ForeignKey(
            "People.Counselor",
            on_delete=models.SET_NULL,
            null=True,
            related_name="student"
        )
        enrollment = models.ManyToManyField(
            Section,
            through=Enrollment,

        )





class CustomPermission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
