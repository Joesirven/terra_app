from django.urls import path

from .views import (
    api_students,
    api_student,
    api_staffs,
    api_staff,
)

urlpatterns = [
    path("students/", api_students, name="api_students",),
    path("students/<str:student_id>/", api_student, name="api_student",),
    path("staff/", api_staffs, name="api_staffs",),
    path("staff/<str:staff_id>/", api_staff, name="api_staff",),
]
