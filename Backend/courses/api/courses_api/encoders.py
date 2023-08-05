from common.json import ModelEncoder, DateEncoder

from .models import Department, Course


class DepartmentEncoder(ModelEncoder):
    model = Department
    properties = [
        "name",
        "description",
        "id",
    ]


class CourseEncoder(ModelEncoder):
    model = Course
    properties = [
        "course_code",
        "name",
        "description",
        "department",
        "credits",
        "is_active",
        "prereqs",
    ]
    encoders = {
        "department": DepartmentEncoder()
    }
