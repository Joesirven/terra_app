from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from django.db import IntegrityError
from .models import Course

from .encoders import (
    DepartmentEncoder,
    CourseEncoder,
)

# api_courses,
@require_http_methods(["GET", "POST"])
def api_courses(request):
    if request.method == "GET":
        courses = Course.objects.all()
        return JsonResponse(
            {"courses": courses},
            encoder=CourseEncoder,
        )

    else: #POST
        try:
            content = json.loads(request.body)
            courses = Course.objects.create(**content)
            return JsonResponse(
                courses,
                encoder=CourseEncoder,
                safe=False,
            )
        except IntegrityError:
            response = JsonResponse(
                {
                    "message": "Course id already exists. Select a unique course id."
                }
            )
            response.status_code = 400
            return response

        except AttributeError:
            response = JsonResponse(
                {"message": "Could not create the course"}
            )
            response.status_code = 400
            return response


@require_http_methods(["DELETE", "GET", "PUT"])
def api_course(request, course_code):
    if request.method == "GET":
        try:
            course = Course.objects.get(course_code=course_code)
            return JsonResponse(
                course,
                encoder=CourseEncoder,
                safe=False,
            )
        except Course.DoesNotExist:
            response = JsonResponse({"message": "Course does not exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            course = Course.objects.get(course_code=course_code)
            course.delete()
            return JsonResponse(
                course,
                encoder=CourseEncoder,
                safe=False,
            )
        except Course.DoesNotExist:
            return JsonResponse({"message": "Course does not exist"})
    else: # PUT
        try:
            content = json.loads(request.body)
            course = Course.objects.get(course_code=course_code)

            props = [
                "course_code",
                "name",
                "description",
                "department",
                "credits",
                "is_active",
                "prereqs",
            ]
            for prop in props:
                if prop in content:
                    setattr(course, prop, content[prop])
            course.save()
            return JsonResponse(
                course,
                encoder=CourseEncoder,
                safe=False,
            )
        except Course.DoesNotExist:
            response = JsonResponse({"message": "Course does not exist"})
            response.status_code = 404
            return response

#DEpartment API
@require_http_methods(["GET", "POST"])
def api_departments(request):
    if request.method == "GET":
        depts = Course.objects.all()
        return JsonResponse(
            {"depts": depts},
            encoder=DepartmentEncoder,
        )

    else: #POST
        try:
            content = json.loads(request.body)
            courses = Course.objects.create(**content)
            return JsonResponse(
                courses,
                encoder=CourseEncoder,
                safe=False,
            )
        except IntegrityError:
            response = JsonResponse(
                {
                    "message": "Course id already exists. Select a unique course id."
                }
            )
            response.status_code = 400
            return response

        except AttributeError:
            response = JsonResponse(
                {"message": "Could not create the course"}
            )
            response.status_code = 400
            return response


@require_http_methods(["DELETE", "GET", "PUT"])
def api_course(request, course_code):
    if request.method == "GET":
        try:
            course = Course.objects.get(course_code=course_code)
            return JsonResponse(
                course,
                encoder=CourseEncoder,
                safe=False,
            )
        except Course.DoesNotExist:
            response = JsonResponse({"message": "Course does not exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            course = Course.objects.get(course_code=course_code)
            course.delete()
            return JsonResponse(
                course,
                encoder=CourseEncoder,
                safe=False,
            )
        except Course.DoesNotExist:
            return JsonResponse({"message": "Course does not exist"})
    else: # PUT
        try:
            content = json.loads(request.body)
            course = Course.objects.get(course_code=course_code)

            props = [
                "course_code",
                "name",
                "description",
                "department",
                "credits",
                "is_active",
                "prereqs",
            ]
            for prop in props:
                if prop in content:
                    setattr(course, prop, content[prop])
            course.save()
            return JsonResponse(
                course,
                encoder=CourseEncoder,
                safe=False,
            )
        except Course.DoesNotExist:
            response = JsonResponse({"message": "Course does not exist"})
            response.status_code = 404
            return response
# api_room,
# api_rooms,
# api_departments,
# api_department,
# api_prereqs,
# api_prereq,
# api_sections,
# api_section,
